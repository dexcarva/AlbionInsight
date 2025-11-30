"""Módulo principal para iniciar a aplicação Albion Insight."""

from .sniffer_manager import SnifferManager
from .ui.main_window import run_app
from .utils.logger import logger


def main():
    """
    Função principal para iniciar a aplicação Albion Insight.
    Orquestra a inicialização da Interface do Usuário.
    O Network Tracker será iniciado a partir da UI.
    """
    logger.info("Albion Insight - Aplicação iniciada (Estrutura Modularizada)")

    # Inicia o gerenciador do sniffer (que inicia o sniffer como subprocesso)
    sniffer_manager = SnifferManager()
    sniffer_manager.start_sniffer()

    # Inicia a aplicação Flet
    run_app(sniffer_manager)

    # Garante que o sniffer seja encerrado ao fechar a UI
    sniffer_manager.stop_sniffer()


if __name__ == "__main__":
    main()
