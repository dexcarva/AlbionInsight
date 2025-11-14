from .models import SessionStats\nimport flet as ft
from ..utils.logger import logger

# Inicializa as estatísticas da sessão
current_session = SessionStats(start_time=0.0)


def start_network_tracker(page: ft.Page):
    """
    Inicia a captura de pacotes de rede.
    """
    logger.info("Network Tracker iniciado. (Scapy)")\n    # TODO: Implementar a lógica de Scapy aqui. O 'page' é passado para que o tracker possa atualizar a UI.
    # TODO: Implementar a lógica de Scapy aqui.
    # Por enquanto, apenas simula a atualização de estatísticas
    current_session.total_silver = 10000
    current_session.total_fame = 5000
    logger.info(
        f"Estatísticas simuladas: "
        f"Silver={current_session.total_silver}, "
        f"Fame={current_session.total_fame}"
    )


def get_current_stats():
    """
    Retorna as estatísticas da sessão atual.
    """
    return current_session
