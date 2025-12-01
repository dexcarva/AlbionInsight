"""Módulo de interface do usuário (UI) da aplicação Albion Insight."""

import flet as ft


def start_ui(page: ft.Page):
    """
    Função principal da interface do usuário (Flet).
    """
    page.title = "Albion Insight"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stats_text = ft.Text("Estatísticas: Aguardando captura...")

    def update_stats(e):
        stats_text.value = "Estatísticas: Capturando dados..."
        page.update()

    page.add(
        ft.Text("Albion Insight - UI (Flet)"),
        ft.ElevatedButton("Atualizar Estatísticas", on_click=update_stats),
        stats_text,
    )


def run_app():
    """
    Inicia a aplicação Flet.
    """
    ft.app(target=start_ui)
