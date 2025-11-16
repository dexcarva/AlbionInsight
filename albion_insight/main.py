from .ui.main_window import run_app
from .utils.logger import logger


def main():
    """
    Função principal para iniciar a aplicação Albion Insight.
    Orquestra a inicialização da Interface do Usuário.
    O Network Tracker será iniciado a partir da UI.
    """
    logger.info("Albion Insight - Aplicação iniciada (Estrutura Modularizada)")

    # Inicia a aplicação Flet
    run_app()

if __name__ == "__main__":
    main()
