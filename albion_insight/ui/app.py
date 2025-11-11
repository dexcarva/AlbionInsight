import flet as ft
from ..core.network_tracker import get_current_stats

def start_ui(page: ft.Page):
    """
    Função principal da interface do usuário (Flet).
    """
    page.title = "Albion Insight"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    stats_text = ft.Text("Estatísticas: Aguardando captura...")

    def update_stats(e):
        stats = get_current_stats()
        stats_text.value = f"Silver: {stats.total_silver}, Fame: {stats.total_fame}"
        page.update()

    page.add(
        ft.Text("Albion Insight - UI (Flet)"),
        ft.ElevatedButton("Atualizar Estatísticas", on_click=update_stats),
        stats_text
    )

def run_app():
    """
    Inicia a aplicação Flet.
    """
    ft.app(target=start_ui)
