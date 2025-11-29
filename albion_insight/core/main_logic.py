"""Módulo principal para iniciar a aplicação Albion Insight."""
from albion_insight.utils.logger import logger
def main():
    """
    Função principal para iniciar a aplicação Albion Insight.
    Orquestra a inicialização da Interface do Usuário.
    O Network Tracker será iniciado a partir da UI.
    """
    logger.info("Albion Insight - Aplicação iniciada (Estrutura Modularizada)")
    # A UI será iniciada pelo __main__.py
if __name__ == "__main__":
    main()

