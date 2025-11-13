import time
from scapy.all import sniff, UDP
from .models import SessionStats
from ..utils.logger import logger

class NetworkTracker:
    """
    Gerencia a captura de pacotes de rede e a atualização das estatísticas da sessão.
    """
    def __init__(self):
        self.current_session = SessionStats(start_time=time.time())
        self.is_running = False
        self.sniff_thread = None

    def _process_packet(self, packet):
        """
        Processa um pacote capturado e atualiza as estatísticas.
        TODO: Implementar a lógica de decodificação do protocolo Photon.
        """
        if UDP in packet:
            # Albion Online usa as portas 5055, 5056, 5058
            if packet[UDP].dport in [5055, 5056, 5058] or packet[UDP].sport in [5055, 5056, 5058]:
                # Simulação de decodificação e atualização de estatísticas
                self.current_session.total_silver += 1 
                self.current_session.total_fame += 2
                # logger.debug(f"Pacote Albion Online capturado. Silver: {self.current_session.total_silver}")
                
    def _sniff_loop(self):
        """
        Loop principal de captura de pacotes.
        """
        logger.info("Iniciando a captura de pacotes com Scapy...")
        # Filtro BPF para as portas de Albion Online
        bpf_filter = "udp and (port 5055 or port 5056 or port 5058)"
        
        try:
            # Usar store=0 para não armazenar pacotes na memória
            sniff(filter=bpf_filter, prn=self._process_packet, store=0, stop_filter=lambda p: not self.is_running)
        except Exception as e:
            logger.error(f"Erro durante a captura de pacotes: {e}")
            self.is_running = False

    def start(self):
        """
        Inicia o rastreador de rede em uma thread separada.
        """
        if not self.is_running:
            self.is_running = True
            import threading
            self.sniff_thread = threading.Thread(target=self._sniff_loop)
            self.sniff_thread.daemon = True # Permite que o programa feche mesmo com a thread rodando
            self.sniff_thread.start()
            logger.info("Network Tracker iniciado em thread separada.")

    def stop(self):
        """
        Para o rastreador de rede.
        """
        if self.is_running:
            self.is_running = False
            # A thread de sniff será interrompida na próxima iteração do stop_filter
            logger.info("Network Tracker parado.")

    def get_current_stats(self):
        """
        Retorna as estatísticas da sessão atual.
        """
        return self.current_session

# Instância global do rastreador para ser usada pela UI
tracker_instance = NetworkTracker()

def start_network_tracker():
    """ Função de compatibilidade para a UI antiga. """
    tracker_instance.start()

def get_current_stats():
    """ Função de compatibilidade para a UI antiga. """
    return tracker_instance.get_current_stats()
