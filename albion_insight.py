#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flet as ft
import os
import sys
import threading
import time
import json
import logging
from datetime import datetime

# Import refactored modules
from network_tracker import NetworkTracker
from models import SessionStats # Importar SessionStats para tipagem, se necessário


# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Application State and UI Logic ---

class DamageMeterEntry(ft.UserControl):
    '''UI control for a single entry in the damage meter.'''
    def __init__(self, name, damage, dps, healing):
        super().__init__()
        self.name = name
        self.damage = damage
        self.dps = dps
        self.healing = healing

    def build(self):
        return ft.Row(
            controls=[
                ft.Text(self.name, width=150, text_align=ft.TextAlign.LEFT),
                ft.Text(f"{self.damage:,}", width=100, text_align=ft.TextAlign.RIGHT),
                ft.Text(f"{self.dps:,.2f}", width=100, text_align=ft.TextAlign.RIGHT),
                ft.Text(f"{self.healing:,}", width=100, text_align=ft.TextAlign.RIGHT),
            ]
        )


class AlbionInsightApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = "Albion Insight"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.START
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window_width = 600
        self.page.window_height = 800
        self.page.on_close = self.on_close
        
        # Initialize NetworkTracker with a callback to update the UI
        self.tracker = NetworkTracker(update_callback=self.update_ui)
        
        # UI Elements
        self.interface_dropdown = ft.Dropdown(
            label="Network Interface",
            options=[ft.dropdown.Option(iface) for iface in self.tracker.get_interfaces()],
            width=200,
            on_change=self.interface_changed
        )
        self.start_button = ft.ElevatedButton(
            "Start Sniffing", 
            icon=ft.icons.PLAY_ARROW_ROUNDED, 
            on_click=self.start_sniffing,
            disabled=True
        )
        self.stop_button = ft.ElevatedButton(
            "Stop Sniffing", 
            icon=ft.icons.STOP_ROUNDED, 
            on_click=self.stop_sniffing,
            disabled=True
        )
        self.reset_button = ft.ElevatedButton(
            "Reset Session", 
            icon=ft.icons.REFRESH_ROUNDED, 
            on_click=self.reset_session,
            disabled=True
        )
        self.save_button = ft.ElevatedButton(
            "Save Session", 
            icon=ft.icons.SAVE_ROUNDED, 
            on_click=self.save_session,
            disabled=True
        )
        self.status_text = ft.Text("Status: Ready", color=ft.colors.GREEN_ACCENT_400)
        self.duration_text = ft.Text("Duration: 00:00:00")
        
        # Damage Meter Header
        self.damage_meter_header = ft.Row(
            controls=[
                ft.Text("Player", weight=ft.FontWeight.BOLD, width=150, text_align=ft.TextAlign.LEFT),
                ft.Text("Damage", weight=ft.FontWeight.BOLD, width=100, text_align=ft.TextAlign.RIGHT),
                ft.Text("DPS", weight=ft.FontWeight.BOLD, width=100, text_align=ft.TextAlign.RIGHT),
                ft.Text("Healing", weight=ft.FontWeight.BOLD, width=100, text_align=ft.TextAlign.RIGHT),
            ],
            spacing=10
        )
        
        # Damage Meter List
        self.damage_meter_list = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True
        )
        
        # Timer for UI updates
        self.timer = threading.Thread(target=self._update_timer_loop, daemon=True)
        self.timer_running = True
        self.timer.start()
        
        # Initial state check
        if self.interface_dropdown.options:
            self.interface_dropdown.value = self.interface_dropdown.options[0].key
            self.start_button.disabled = False
        else:
            self.status_text.value = "Status: No network interfaces found."
            self.status_text.color = ft.colors.RED_500
            
    def build(self):
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.interface_dropdown,
                            self.start_button,
                            self.stop_button,
                            self.reset_button,
                            self.save_button,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    ft.Row(
                        controls=[
                            self.status_text,
                            self.duration_text,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Divider(),
                    self.damage_meter_header,
                    ft.Divider(),
                    self.damage_meter_list,
                ],
                expand=True
            )
        )

    def interface_changed(self, e):
        self.start_button.disabled = False
        self.update()

    def start_sniffing(self, e):
        interface = self.interface_dropdown.value
        if not interface:
            self.status_text.value = "Status: Please select a network interface."
            self.status_text.color = ft.colors.RED_500
            self.update()
            return
            
        self.tracker.start_sniffing(interface)
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.reset_button.disabled = False
        self.save_button.disabled = False
        self.status_text.value = f"Status: Sniffing on {interface}..."
        self.status_text.color = ft.colors.BLUE_ACCENT_400
        self.update()

    def stop_sniffing(self, e):
        self.tracker.stop_sniffing()
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.status_text.value = "Status: Stopped."
        self.status_text.color = ft.colors.ORANGE_ACCENT_400
        self.update()

    def reset_session(self, e):
        self.tracker.reset_session()
        self.update_ui() # Force immediate UI update
        self.page.snack_bar = ft.SnackBar(ft.Text("Session reset."), open=True)
        self.page.update()

    def save_session(self, e):
        filename = self.tracker.save_session()
        if filename:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Session saved to {filename}"), open=True)
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Error saving session."), open=True)
        self.page.update()

    def update_ui(self):
        '''Updates the damage meter list and duration text.'''
        data = self.tracker.get_damage_meter_data()
        
        self.damage_meter_list.controls.clear()
        
        for entry in data:
            self.damage_meter_list.controls.append(
                DamageMeterEntry(
                    name=entry["name"],
                    damage=entry["damage"],
                    dps=entry["dps"],
                    healing=entry["healing"]
                )
            )
            
        self.duration_text.value = f"Duration: {self.tracker.get_session_duration()}"
        
        # Ensure the UI update is run on the main thread
        self.page.run_thread(self.update)

    def _update_timer_loop(self):
        '''Background thread to periodically update the UI for duration and DPS.'''
        while self.timer_running:
            time.sleep(1)
            if self.tracker.session_stats.is_running:
                self.update_ui()

    def on_close(self, e):
        '''Stops the sniffing and the timer thread when the window is closed.'''
        self.timer_running = False
        self.tracker.stop_sniffing()
        self.page.update()

def main(page: ft.Page):
    # The original code had a lot of logic here, now it's just the app setup
    app = AlbionInsightApp(page)
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
