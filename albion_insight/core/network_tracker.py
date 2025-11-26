"""Módulo de rastreamento de rede da aplicação Albion Insight."""

import threading
import time

from scapy.all import IP, UDP, sniff

from albion_insight.core.models import SessionStats
from albion_insight.utils.logger import logger

# Variável global para controlar o estado do rastreador
is_sniffing = threading.Event()

# Inicializa as estatísticas da sessão
current_session = SessionStats(start_time=0.0)


def process_packet(packet):
    """Processa um pacote capturado pelo Scapy."""
    if UDP in packet and IP in packet:
        # Aqui entra a lógica de decodificação do protocolo Photon
        # Por enquanto, apenas logamos que um pacote foi recebido
        logger.debug(
            f"Pacote Albion Online recebido de {packet[IP].src}:{packet[UDP].sport} "
            f"para {packet[IP].dst}:{packet[IP].dport}"
        )
        # Simulação de atualização de estatísticas (a ser substituída pela lógica real)
        global current_session
        current_session.total_silver += 1
        current_session.total_fame += 1


def network_tracker_thread(interface: str):
    """
    Função que roda em uma thread separada para capturar pacotes de rede.
    """
    logger.info(f"Network Tracker iniciado em thread separada na interface: {interface}")

    # Filtro BPF (Berkeley Packet Filter) para pacotes UDP nas portas do Albion Online
    bpf_filter = "udp and (port 5055 or port 5056 or port 5058)"  # Filtro BPF para Albion Online

    while is_sniffing.is_set():
        try:
            # Sniff é bloqueante, o timeout permite que o loop verifique is_sniffing.is_set()
            sniff(prn=process_packet, filter=bpf_filter, iface=interface, store=0, timeout=1)
        except Exception as e:
            logger.error(f"Erro durante a captura de pacotes: {e}")
            time.sleep(1)  # Pausa em caso de erro

    logger.info("Network Tracker parado.")


def start_network_tracker(interface: str = None):
    """
    Inicia a captura de pacotes de rede em uma thread separada.

    :param interface: A interface de rede a ser usada para o sniffing.
        Se None, Scapy tentará adivinhar.
    """
    global current_session
    current_session = SessionStats(start_time=time.time())
    is_sniffing.set()  # Sinaliza que o rastreador deve rodar

    # Cria e inicia a thread do tracker
    tracker_thread = threading.Thread(target=network_tracker_thread, args=(interface,), daemon=True)
    tracker_thread.start()


def stop_network_tracker():
    """Para a captura de pacotes de rede."""
    is_sniffing.clear()  # Sinaliza que o rastreador deve parar
    logger.info("Sinal de parada enviado ao Network Tracker.")


def get_current_stats():
    """
    Retorna as estatísticas da sessão atual.
    """
    return current_session
