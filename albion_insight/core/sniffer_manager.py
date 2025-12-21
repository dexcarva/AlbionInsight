import sys
import threading
import subprocess
import signal

from ..utils.logger import logger


class SnifferManager:
    """
    Gerencia o subprocesso do sniffer de pacotes (que requer privilégios de root).
    """

    def __init__(self):
        self.sniffer_process = None
        self.output_thread = None
        self.is_running = False
        self.data_queue = []  # Fila simples para simular a passagem de dados

    def _read_output(self):
        """Lê a saída do subprocesso e a coloca na fila."""
        logger.info("Thread de leitura de saída do sniffer iniciada.")
        while self.is_running and self.sniffer_process and self.sniffer_process.stdout:
            try:
                line = self.sniffer_process.stdout.readline()
                if not line:
                    break
                line = line.decode("utf-8")
                if line:
                    logger.debug(f"Sniffer Output: {line}")
                    self.data_queue.append(line)
            except Exception as e:
                logger.error(f"Erro ao ler saída do sniffer: {e}")
                break
        logger.info("Thread de leitura de saída do sniffer encerrada.")

    def start_sniffer(self):
        """Inicia o sniffer como um subprocesso com privilégios de root (sudo)."""
        if self.is_running:
            logger.warning("Sniffer já está em execução.")
            return

        # Comando para executar o sniffer_process.py com sudo
        # Usamos sys.executable para garantir que o mesmo interpretador Python seja usado
        command = [
            "sudo",
            sys.executable,
            "-m",
            "albion_insight.core.sniffer_process",  # Executa o módulo
        ]

        try:
            logger.info(f"Iniciando sniffer com comando: {' '.join(command)}")
            self.sniffer_process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                bufsize=1,  # Linha por linha
                universal_newlines=False,  # Manter como bytes para decodificação manual
            )
            self.is_running = True

            # Inicia a thread para ler a saída do sniffer
            self.output_thread = threading.Thread(target=self._read_output)
            self.output_thread.daemon = True
            self.output_thread.start()

            logger.info("Sniffer iniciado com sucesso.")
        except FileNotFoundError:
            logger.error(
                "Erro: 'sudo' ou 'python' não encontrado. Certifique-se de que estão no PATH."
            )
            self.is_running = False
        except Exception as e:
            logger.error(f"Erro ao iniciar o sniffer: {e}")
            self.is_running = False

    def stop_sniffer(self):
        """Encerra o subprocesso do sniffer."""
        if self.sniffer_process and self.sniffer_process.poll() is None:
            logger.info("Encerrando sniffer...")
            try:
                # Envia um sinal de interrupção (Ctrl+C) para o processo
                self.sniffer_process.send_signal(subprocess.signal.SIGINT)
                self.sniffer_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                logger.warning("Sniffer não respondeu ao SIGINT, forçando encerramento (SIGKILL).")
                self.sniffer_process.kill()
            except Exception as e:
                logger.error(f"Erro ao encerrar sniffer: {e}")
            finally:
                self.is_running = False
                if self.output_thread and self.output_thread.is_alive():
                    self.output_thread.join(timeout=1)
                logger.info("Sniffer encerrado.")
        elif self.is_running:
            self.is_running = False
            logger.info("Sniffer já estava encerrado.")

    def get_latest_data(self):
        """Retorna os dados mais recentes da fila e limpa a fila."""
        data = self.data_queue
        self.data_queue = []
        return data
