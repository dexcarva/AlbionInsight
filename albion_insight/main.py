from .ui.app import run_app
from .utils.logger import logger
from .core.network_tracker import start_network_tracker

def main():
    """
    Função principal para iniciar a aplicação Albion Insight.
    Orquestra a inicialização do Network Tracker e da Interface do Usuário.
    """
    logger.info("Albion Insight - Aplicação iniciada (Estrutura Modularizada)")
    
    # O Network Tracker deve ser iniciado em uma thread separada,
    # mas por enquanto, apenas chamamos a função para demonstrar a estrutura.
    start_network_tracker()
    
    # Inicia a aplicação Flet
    run_app()
