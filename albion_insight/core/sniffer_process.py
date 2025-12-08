
from albion_insight.core.network_tracker import main as network_tracker_main

# Este módulo deve ser executado com privilégios de root/administrador
# para usar Scapy e capturar pacotes de rede.


def run_sniffer():
    """
    Função que inicia o sniffer de pacotes real.
    Este módulo é o ponto de entrada para o subprocesso executado com 'sudo'.
    Ele chama a lógica principal do sniffer (network_tracker.py).
    """
    # A verificação de root é feita dentro de network_tracker.main()
    network_tracker_main()


if __name__ == "__main__":
    run_sniffer()
