from .models import SessionStats
from ..utils.logger import logger

# Inicializa as estatísticas da sessão
current_session = SessionStats(start_time=0.0)

def start_network_tracker():
    """
    Inicia a captura de pacotes de rede.
    """
    logger.info("Network Tracker iniciado. (Scapy)")
    # TODO: Implementar a lógica de Scapy aqui.
    # Por enquanto, apenas simula a atualização de estatísticas
    current_session.total_silver = 10000
    current_session.total_fame = 5000
    logger.info(f"Estatísticas simuladas: Silver={current_session.total_silver}, Fame={current_session.total_fame}")

def get_current_stats():
    """
    Retorna as estatísticas da sessão atual.
    """
    return current_session
