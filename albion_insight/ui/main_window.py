"""Módulo da janela principal da aplicação Albion Insight."""

import flet as ft


def start_ui(page: ft.Page, sniffer_manager):
    # O Network Tracker é gerenciado pelo SnifferManager passado como argumento
    """
    Função principal da interface do usuário (Flet).
    """
    page.title = "Albion Insight"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stats_text = ft.Text("Estatísticas: Aguardando captura...")

    def update_stats(e):
        # Pega os dados do sniffer_manager
        data = sniffer_manager.get_latest_data()
        if data:
            # Simplesmente exibe o último evento simulado
            last_event = data[-1]
            stats_text.value = f"Último Evento: {last_event}"
        else:
            stats_text.value = "Estatísticas: Aguardando dados do sniffer..."
        page.update()

    page.add(
        ft.Text("Albion Insight - UI (Flet)"),
        ft.ElevatedButton("Atualizar Estatísticas", on_click=update_stats),
        stats_text,
    )


def run_app(sniffer_manager):
    """
    Inicia a aplicação Flet, passando o SnifferManager.
    """
    # Cria uma função lambda para passar o sniffer_manager para start_ui
    ft.app(target=lambda page: start_ui(page, sniffer_manager))
