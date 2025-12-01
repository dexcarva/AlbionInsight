"""Módulo de rastreamento de rede da aplicação Albion Insight."""

import os
import sys
from datetime import datetime

from scapy.all import IP, UDP, get_if_list, sniff

from albion_insight.utils.logger import logger

# Variável global para controlar o estado do rastreador


# Inicializa as estatísticas da sessão


# O sniffer agora é um script autônomo que se comunica via stdout
# Ele não precisa mais de threads, pois será um subprocesso dedicado.


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
        # print("DATA:SILVER:1")
        # print("DATA:FAME:1")


def run_network_tracker(interface: str):
    """
    Função que roda em uma thread separada para capturar pacotes de rede.
    """
    logger.info(f"Network Tracker iniciado em thread separada na interface: {interface}")

    # Filtro BPF (Berkeley Packet Filter) para pacotes UDP nas portas do Albion Online
    bpf_filter = "udp and (port 5055 or port 5056 or port 5058)"  # Filtro BPF para Albion Online

    # Sniff é bloqueante. Ele só para com um KeyboardInterrupt (SIGINT)
    try:
        sniff(prn=process_packet, filter=bpf_filter, iface=interface, store=0)
    except Exception as e:
        logger.error(f"Erro durante a captura de pacotes: {e}")

    logger.info("Network Tracker parado.")


def get_interface():
    """Tenta adivinhar a interface de rede."""
    # Lógica simplificada para encontrar uma interface ativa
    interfaces = get_if_list()
    # Tenta encontrar uma interface que não seja loopback e não seja 'any'
    for iface in interfaces:
        if iface != "lo" and iface != "any":
            return iface
    return "any"


def main():
    """Ponto de entrada para o processo sniffer."""
    if os.geteuid() != 0:
        logger.error("O sniffer deve ser executado como root/administrador.")
        sys.exit(1)

    interface = get_interface()
    logger.info(f"Sniffer iniciado em {datetime.now().isoformat()} na interface {interface}")
    sys.stdout.flush()

    run_network_tracker(interface)


if __name__ == "__main__":
    main()
