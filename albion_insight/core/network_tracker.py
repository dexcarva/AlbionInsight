from .models import SessionStats
import flet as ft
import threading
import time
from ..utils.logger import logger

# Inicializa as estatísticas da sessão
current_session = SessionStats(start_time=0.0)


def network_tracker_thread(page: ft.Page):
    """
    Função que roda em uma thread separada para simular a captura de pacotes.
    """
    logger.info("Network Tracker iniciado em thread separada. (Simulação Scapy)")
    
    # Simulação de captura de pacotes e atualização de estatísticas
    silver_counter = 0
    fame_counter = 0
    
    while True:
        # Simula a decodificação de um pacote
        silver_counter += 100
        fame_counter += 50
        
        current_session.total_silver = silver_counter
        current_session.total_fame = fame_counter
        
        # A UI será atualizada pelo botão, mas a thread de rede está rodando
        logger.debug(f"Estatísticas atualizadas: Silver={silver_counter}, Fame={fame_counter}")
        
        time.sleep(5) # Simula o intervalo entre pacotes ou atualizações

def start_network_tracker(page: ft.Page):
    """
    Inicia a captura de pacotes de rede em uma thread separada.
    """
    # Cria e inicia a thread do tracker
    tracker_thread = threading.Thread(target=network_tracker_thread, args=(page,), daemon=True)
    tracker_thread.start()


def get_current_stats():
    """
    Retorna as estatísticas da sessão atual.
    """
    return current_session
