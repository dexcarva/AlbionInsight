# -*- coding: utf-8 -*-
import flet as ft
import os
import sys
import threading
import time
import json
import logging
from scapy.all import sniff, UDP, IP
from collections import defaultdict
from datetime import datetime, timedelta

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Constants and Configuration ---
# Albion Online UDP Ports (based on C# code analysis)
ALBION_PORTS = {5055, 5056, 5058}
# Photon header codes (based on C# code analysis)
PHOTON_HEADERS = {0xF1, 0xF2, 0xFE}
DATA_DIR = os.path.expanduser("~/.albion_insight")

# --- Model Classes ---

class DamageMeterEntry:
    def __init__(self, player_name):
        self.player_name = player_name
        self.damage_done = 0
        self.damage_taken = 0
        self.healing_done = 0
        self.healing_taken = 0
        self.kills = 0
        self.deaths = 0

    def update_damage_done(self, amount):
        self.damage_done += amount

    def update_healing_done(self, amount):
        self.healing_done += amount

    def get_dps(self, elapsed_time):
        return self.damage_done / elapsed_time if elapsed_time > 0 else 0

    def to_dict(self):
        return {
            "player_name": self.player_name,
            "damage_done": self.damage_done,
            "damage_taken": self.damage_taken,
            "healing_done": self.healing_done,
            "healing_taken": self.healing_taken,
            "kills": self.kills,
            "deaths": self.deaths,
        }

class LiveStats:
    def __init__(self):
        self.silver_gained = 0
        self.fame_gained = 0
        self.kills = 0
        self.deaths = 0
        self.looted_chests = 0
        self.re_spec_points = 0
        self.repair_costs = 0
        self.faction_points = 0
        self.start_time = time.time()
        self.session_start = datetime.now()
        self.notifications = []
        self.damage_meter = defaultdict(lambda: DamageMeterEntry("Unknown Player")) # Damage Meter structure

    def reset(self):
        self.silver_gained = 0
        self.fame_gained = 0
        self.kills = 0
        self.deaths = 0
        self.looted_chests = 0
        self.re_spec_points = 0
        self.repair_costs = 0
        self.faction_points = 0
        self.start_time = time.time()
        self.session_start = datetime.now()
        self.damage_meter.clear()

    def get_time_elapsed(self):
        return time.time() - self.start_time

    def get_stats_per_hour(self):
        elapsed_hours = self.get_time_elapsed() / 3600
        if elapsed_hours == 0:
            return defaultdict(lambda: 0)
        return {
            "silver": self.silver_gained / elapsed_hours if elapsed_hours > 0 else 0,
            "fame": self.fame_gained / elapsed_hours if elapsed_hours > 0 else 0,
            "kills": self.kills / elapsed_hours if elapsed_hours > 0 else 0,
        }

    def add_notification(self, message, notification_type="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.notifications.append({
            "timestamp": timestamp,
            "message": message,
            "type": notification_type
        })
        # Keep only the last 100 events
        if len(self.notifications) > 100:
            self.notifications.pop(0)

    def save_to_file(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        filename = os.path.join(DATA_DIR, f"session_{self.session_start.strftime('%Y%m%d_%H%M%S')}.json")
        data = {
            "session_start": self.session_start.isoformat(),
            "silver_gained": self.silver_gained,
            "fame_gained": self.fame_gained,
            "kills": self.kills,
            "deaths": self.deaths,
            "looted_chests": self.looted_chests,
            "re_spec_points": self.re_spec_points,
            "repair_costs": self.repair_costs,
            "faction_points": self.faction_points,
            "time_elapsed": self.get_time_elapsed(),
            "damage_meter": [entry.to_dict() for entry in self.damage_meter.values()]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Session saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving session: {e}")

# --- Network Tracking Logic ---
class NetworkTracker:
    def __init__(self, stats_model):
        self.stats_model = stats_model
        self.stop_event = threading.Event()
        self.thread = None

    def start_tracking(self, interface=None):
        if self.thread and self.thread.is_alive():
            logger.warning("Tracking already running.")
            return

        self.stats_model.reset() # Reset stats on start
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._sniff_loop, args=(interface,))
        self.thread.daemon = True
        self.thread.start()
        logger.info("Tracking started.")

    def stop_tracking(self):
        self.stop_event.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2)
        logger.info("Tracking stopped.")

    def _sniff_loop(self, interface):
        try:
            # BPF filter to capture only UDP packets on Albion ports
            ports_str = " or ".join([f"port {p}" for p in ALBION_PORTS])
            bpf_filter = f"udp and ({ports_str})"

            sniff(filter=bpf_filter, prn=self._process_packet, iface=interface, stop_filter=lambda x: self.stop_event.is_set(), store=False)
        except Exception as e:
            logger.error(f"Error in sniffing loop: {e}")

    def _process_packet(self, packet):
        if not packet.haslayer(UDP):
            return

        udp_layer = packet[UDP]
        payload = bytes(udp_layer.payload)

        if udp_layer.sport not in ALBION_PORTS and udp_layer.dport not in ALBION_PORTS:
            return

        if not payload or payload[0] not in PHOTON_HEADERS:
            return

        # SIMULATION: Replace this with actual Photon decoding logic
        self._simulate_stat_update(payload)
        self._simulate_damage_meter_update(payload)

    def _simulate_stat_update(self, payload):
        # Simulation of stat update based on payload length
        if len(payload) > 5:
            event_type = payload[1] % 10  # Simulate different event types
            
            if event_type == 0:
                self.stats_model.silver_gained += 100
                self.stats_model.add_notification("Silver gained: +100", "silver")
            elif event_type == 1:
                self.stats_model.fame_gained += 50
                self.stats_model.add_notification("Fame gained: +50", "fame")
            elif event_type == 2:
                self.stats_model.kills += 1
                self.stats_model.add_notification("Kill recorded", "kill")
            elif event_type == 3:
                self.stats_model.deaths += 1
                self.stats_model.add_notification("Death recorded", "death")
            elif event_type == 4:
                self.stats_model.looted_chests += 1
                self.stats_model.add_notification("Chest looted", "loot")

    def _simulate_damage_meter_update(self, payload):
        # SIMULATION: Damage Meter update logic
        if len(payload) > 10:
            player_id = payload[2] % 3 # Simulate 3 players
            player_name = f"Player {player_id}"
            
            entry = self.stats_model.damage_meter[player_name]
            entry.player_name = player_name # Update name in case it was the default "Unknown Player"
            
            # Simulate damage done and healing done
            if payload[3] % 2 == 0:
                entry.update_damage_done(500 + payload[4])
                self.stats_model.add_notification(f"{player_name} dealt damage", "damage")
            else:
                entry.update_healing_done(100 + payload[5])
                self.stats_model.add_notification(f"{player_name} healed", "healing")

# --- User Interface (Flet) ---
class AlbionInsightApp:
    def __init__(self):
        self.stats = LiveStats()
        self.tracker = NetworkTracker(self.stats)
        self.page = None
        self.is_tracking = False
        self.setup_ui_elements()
        self.timer_thread = threading.Thread(target=self._update_ui_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def setup_ui_elements(self):
        # Dashboard Tab
        self.silver_text = ft.Text(f"Silver: {self.stats.silver_gained}")
        self.fame_text = ft.Text(f"Fame: {self.stats.fame_gained}")
        self.kills_text = ft.Text(f"Kills: {self.stats.kills}")
        self.deaths_text = ft.Text(f"Deaths: {self.stats.deaths}")
        self.looted_chests_text = ft.Text(f"Looted Chests: {self.stats.looted_chests}")
        self.time_elapsed_text = ft.Text(f"Time: 00:00:00")
        self.silver_per_hour_text = ft.Text(f"Silver/Hour: 0")
        self.fame_per_hour_text = ft.Text(f"Fame/Hour: 0")
        
        # Damage Meter Table
        self.damage_meter_data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Player")),
                ft.DataColumn(ft.Text("Damage Done"), numeric=True),
                ft.DataColumn(ft.Text("DPS"), numeric=True),
                ft.DataColumn(ft.Text("Healing Done"), numeric=True),
            ],
            rows=[],
        )
        
        # Buttons
        self.start_button = ft.ElevatedButton("Start Tracking", on_click=self.start_tracking_click)
        self.stop_button = ft.ElevatedButton("Stop Tracking", on_click=self.stop_tracking_click, disabled=True)
        self.reset_button = ft.ElevatedButton("Reset Stats", on_click=self.reset_stats_click)
        self.save_button = ft.ElevatedButton("Save Session", on_click=self.save_session_click)
        
        # Interface Selection
        self.interface_dropdown = ft.Dropdown(
            label="Network Interface",
            options=[
                ft.dropdown.Option("eth0"),
                ft.dropdown.Option("wlan0"),
                ft.dropdown.Option("lo"),
            ],
            value="eth0"
        )
        
        # Notifications List
        self.notifications_list = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
        )
        
        # Status
        self.status_text = ft.Text("Status: Stopped", color=ft.Colors.RED_500)

    def _update_ui_timer(self):
        while True:
            if self.page:
                try:
                    # Update stats
                    self.silver_text.value = f"Silver: {self.stats.silver_gained}"
                    self.fame_text.value = f"Fame: {self.stats.fame_gained}"
                    self.kills_text.value = f"Kills: {self.stats.kills}"
                    self.deaths_text.value = f"Deaths: {self.stats.deaths}"
                    self.looted_chests_text.value = f"Looted Chests: {self.stats.looted_chests}"
                    
                    # Calculate elapsed time
                    elapsed = self.stats.get_time_elapsed()
                    hours, remainder = divmod(int(elapsed), 3600)
                    minutes, seconds = divmod(remainder, 60)
                    self.time_elapsed_text.value = f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}"
                    
                    # Calculate stats per hour
                    stats_per_hour = self.stats.get_stats_per_hour()
                    self.silver_per_hour_text.value = f"Silver/Hour: {int(stats_per_hour['silver'])}"
                    self.fame_per_hour_text.value = f"Fame/Hour: {int(stats_per_hour['fame'])}"
                    
                    # Update Damage Meter Table
                    self.damage_meter_data_table.rows.clear()
                    elapsed_time = self.stats.get_time_elapsed()
                    sorted_entries = sorted(self.stats.damage_meter.values(), key=lambda x: x.damage_done, reverse=True)
                    
                    for entry in sorted_entries:
                        dps = entry.get_dps(elapsed_time)
                        self.damage_meter_data_table.rows.append(
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(entry.player_name)),
                                    ft.DataCell(ft.Text(f"{entry.damage_done:,}")),
                                    ft.DataCell(ft.Text(f"{dps:,.2f}")),
                                    ft.DataCell(ft.Text(f"{entry.healing_done:,}")),
                                ]
                            )
                        )
                    
                    # Update notifications
                    self.notifications_list.controls.clear()
                    for notif in self.stats.notifications[-10:]:  # Show last 10
                        self.notifications_list.controls.append(
                            ft.Text(f"[{notif['timestamp']}] {notif['message']}", size=12)
                        )
                    
                    self.page.update()
                except Exception as e:
                    logger.error(f"Error updating UI: {e}")
                    break
            time.sleep(1)

    def start_tracking_click(self, e):
        interface = self.interface_dropdown.value
        
        # Check for root/admin privileges needed for network sniffing
        if sys.platform.startswith('linux') and os.geteuid() != 0:
            self.status_text.value = "Status: Error (Root/Admin required on Linux)"
            self.status_text.color = ft.Colors.RED_500
            self.page.update()
            return
            
        self.tracker.start_tracking(interface)
        self.is_tracking = True
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.status_text.value = f"Status: Tracking on {interface}..."
        self.status_text.color = ft.Colors.GREEN_500
        self.page.update()

    def stop_tracking_click(self, e):
        self.tracker.stop_tracking()
        self.is_tracking = False
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.status_text.value = "Status: Stopped"
        self.status_text.color = ft.Colors.RED_500
        self.page.update()

    def reset_stats_click(self, e):
        self.stats.reset()
        self.page.update()

    def save_session_click(self, e):
        self.stats.save_to_file()
        self.status_text.value = "Status: Session saved"
        self.page.update()

    def main(self, page: ft.Page):
        self.page = page
        page.title = "Albion Insight"
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window_width = 800
        page.window_height = 600
        
        # Dashboard Tab
        dashboard_tab = ft.Tab(
            text="Dashboard",
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Live Statistics", size=20, weight=ft.FontWeight.BOLD),
                        ft.Row([self.silver_text, self.silver_per_hour_text]),
                        ft.Row([self.fame_text, self.fame_per_hour_text]),
                        ft.Row([self.kills_text, self.deaths_text]),
                        ft.Row([self.looted_chests_text, self.time_elapsed_text]),
                        ft.Divider(),
                        ft.Text("Controls", size=16, weight=ft.FontWeight.BOLD),
                        self.interface_dropdown,
                        ft.Row([self.start_button, self.stop_button, self.reset_button, self.save_button]),
                        self.status_text,
                    ],
                    spacing=10,
                ),
                padding=20,
            )
        )
        
        # Damage Meter Tab
        damage_meter_tab = ft.Tab(
            text="Damage Meter",
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Live Combat Statistics", size=20, weight=ft.FontWeight.BOLD),
                        ft.Container(
                            content=self.damage_meter_data_table,
                            expand=True,
                            padding=ft.padding.only(top=10),
                        )
                    ],
                    spacing=10,
                    expand=True,
                ),
                padding=20,
                expand=True,
            )
        )
        
        # Logging Tab
        logging_tab = ft.Tab(
            text="Event Log",
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Recent Events", size=20, weight=ft.FontWeight.BOLD),
                        self.notifications_list,
                    ],
                    spacing=10,
                    expand=True,
                ),
                padding=20,
                expand=True,
            )
        )
        
        # Settings Tab
        settings_tab = ft.Tab(
            text="Settings",
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Settings", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("More settings coming soon...", size=14),
                    ],
                    spacing=10,
                ),
                padding=20,
            )
        )
        
        # Tabs
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[dashboard_tab, damage_meter_tab, logging_tab, settings_tab],
            expand=True,
        )
        
        page.add(tabs)

# --- Entry Point ---
if __name__ == "__main__":
    app = AlbionInsightApp()
    # Use view=ft.WEB_BROWSER for web-based execution (like in the sandbox)
    # For local desktop execution, use view=ft.FLET_APP()
    ft.app(target=app.main, view=ft.WEB_BROWSER, port=8000)

