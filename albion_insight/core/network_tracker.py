"""Módulo de rastreamento de rede da aplicação Albion Insight."""

import os
import sys
from datetime import datetime

from scapy.all import get_if_list, sniff  # type: ignore
from scapy.layers.inet import IP, UDP\n\nfrom .protocol_decoder import ProtocolDecoder\nfrom .models import SessionStats

from albion_insight.utils.logger import logger

# Variável global para controlar o estado do rastreador\n\ncurrent_session = SessionStats()\nprotocol_decoder = ProtocolDecoder(current_session)


# Inicializa as estatísticas da sessão


# O sniffer agora é um script autônomo que se comunica via stdout
# Ele não precisa mais de threads, pois será um subprocesso dedicado.


def process_packet(packet):
    """Processa um pacote capturado pelo Scapy."""
    if UDP in packet and IP in packet:
        # Aqui entra a lógica de decodificação do protocolo Photon
        # Tenta decodificar o pacote com a lógica do Photon\n        # A decodificação real deve ser implementada em ProtocolDecoder\n        if protocol_decoder.decode_and_update(bytes(packet)):\n            # Se decodificado com sucesso, envia um sinal para a UI\n            # No futuro, o ProtocolDecoder enviará os dados diretamente para a UI\n            print(f"DATA:SILVER:{current_session.total_silver}")\n            sys.stdout.flush()
        logger.debug(
            "Pacote Albion Online recebido de %s:%s para %s:%s",
            packet[IP].src,
            packet[UDP].sport,
            packet[IP].dst,
            packet[IP].dport,
        )
        # Simulação de atualização de estatísticas (a ser substituída pela lógica real)
        # print("DATA:SILVER:1")
        # print("DATA:FAME:1")


def run_network_tracker(interface: str):
    """
    Função que roda em uma thread separada para capturar pacotes de rede.
    """
    logger.info("Network Tracker iniciado em thread separada na interface: %s", interface)

    # Filtro BPF (Berkeley Packet Filter) para pacotes UDP nas portas do Albion Online
    bpf_filter = "udp and (port 5055 or port 5056 or port 5058)"  # Filtro BPF para Albion Online

    # Sniff é bloqueante. Ele só para com um KeyboardInterrupt (SIGINT)
    try:
        sniff(prn=process_packet, filter=bpf_filter, iface=interface, store=0)
    except OSError as e:
        # OSError é comum quando o usuário não tem permissão ou a interface é inválida
        logger.error("Erro de permissão ou interface durante a captura de pacotes: %s", e)
        # Re-lança para ser capturado pelo processo pai, se necessário
        raise
    except Exception as e:
        logger.error("Erro inesperado durante a captura de pacotes: %s", e)
        raise

    logger.info("Network Tracker parado.")


def get_interface():
    """Tenta adivinhar a interface de rede."""
    # Lógica simplificada para encontrar uma interface ativa
    interfaces = get_if_list()
    # Tenta encontrar uma interface que não seja loopback e não seja 'any'
    # Usando 'not in' para melhor legibilidade (R1714)
    for iface in interfaces:
        if iface not in ("lo", "any"):
            return iface
    return "any"


def main():
    """Ponto de entrada para o processo sniffer."""
    if os.geteuid() != 0:
        logger.error("O sniffer deve ser executado como root/administrador.")
        sys.exit(1)

    interface = get_interface()
    logger.info("Sniffer iniciado em %s na interface %s", datetime.now().isoformat(), interface)
    sys.stdout.flush()

    run_network_tracker(interface)


if __name__ == "__main__":
    main()
