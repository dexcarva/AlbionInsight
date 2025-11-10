import flet as ft

def start_ui(page: ft.Page):
    """
    Função principal da interface do usuário (Flet).
    """
    page.title = "Albion Insight"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Text("Albion Insight - UI (Flet)"),
        ft.ElevatedButton("Iniciar Captura de Pacotes", on_click=lambda e: print("Iniciando captura..."))
    )

def run_app():
    """
    Inicia a aplicação Flet.
    """
    ft.app(target=start_ui)
