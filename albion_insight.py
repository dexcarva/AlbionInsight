#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flet as ft
import os
import sys
import threading
import time
import json
import logging
import struct
from enum import Enum
from scapy.all import sniff, UDP, IP
from collections import defaultdict
from datetime import datetime, timedelta

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Photon Protocol Decoding Logic (Translated from C# Protocol16Deserializer) ---

class Protocol16Type(Enum):
    Unknown = 0
    Null = 42
    Dictionary = 68
    StringArray = 97
    Byte = 98
    Double = 100
    EventData = 101
    Float = 102
    Integer = 105
    Hashtable = 104
    Short = 107
    Long = 108
    IntegerArray = 110
    Boolean = 111
    OperationResponse = 112
    OperationRequest = 113
    String = 115
    ByteArray = 120
    Array = 121
    ObjectArray = 122

class PhotonParser:
    def __init__(self, payload):
        self.payload = payload
        self.offset = 0

    def read(self, count):
        if self.offset + count > len(self.payload):
            raise ValueError("Not enough data to read")
        data = self.payload[self.offset:self.offset + count]
        self.offset += count
        return data

    def deserialize(self):
        type_code = self.deserialize_byte()
        return self._deserialize(type_code)

    def _deserialize(self, type_code):
        if type_code == Protocol16Type.Null.value:
            return None
        elif type_code == Protocol16Type.Byte.value:
            return self.deserialize_byte()
        elif type_code == Protocol16Type.Short.value:
            return self.deserialize_short()
        elif type_code == Protocol16Type.Integer.value:
            return self.deserialize_integer()
        elif type_code == Protocol16Type.Long.value:
            return self.deserialize_long()
        elif type_code == Protocol16Type.Float.value:
            return self.deserialize_float()
        elif type_code == Protocol16Type.Double.value:
            return self.deserialize_double()
        elif type_code == Protocol16Type.String.value:
            return self.deserialize_string()
        elif type_code == Protocol16Type.Boolean.value:
            return self.deserialize_boolean()
        elif type_code == Protocol16Type.Dictionary.value:
            return self.deserialize_dictionary()
        elif type_code == Protocol16Type.Hashtable.value:
            return self.deserialize_hashtable()
        elif type_code == Protocol16Type.StringArray.value:
            return self.deserialize_string_array()
        elif type_code == Protocol16Type.ByteArray.value:
            return self.deserialize_byte_array()
        elif type_code == Protocol16Type.ObjectArray.value:
            return self.deserialize_object_array()
        elif type_code == Protocol16Type.EventData.value:
            return self.deserialize_event_data()
        elif type_code == Protocol16Type.OperationRequest.value:
            return self.deserialize_operation_request()
        elif type_code == Protocol16Type.OperationResponse.value:
            return self.deserialize_operation_response()
        else:
            # Fallback for unknown types or complex arrays/types not fully translated
            logger.warning(f"Unsupported type code: {type_code}. Skipping {self.offset}")
            return None

    def deserialize_byte(self):
        return self.read(1)[0]

    def deserialize_short(self):
        return struct.unpack(">h", self.read(2))[0]

    def deserialize_integer(self):
        return struct.unpack(">i", self.read(4))[0]

    def deserialize_long(self):
        return struct.unpack(">q", self.read(8))[0]

    def deserialize_float(self):
        return struct.unpack(">f", self.read(4))[0]

    def deserialize_double(self):
        return struct.unpack(">d", self.read(8))[0]

    def deserialize_boolean(self):
        return self.deserialize_byte() != 0

    def deserialize_string(self):
        string_size = self.deserialize_short()
        if string_size == 0:
            return ""
        return self.read(string_size).decode("utf-8")

    def deserialize_dictionary(self):
        key_type_code = self.deserialize_byte()
        value_type_code = self.deserialize_byte()
        dictionary_size = self.deserialize_short()
        dictionary = {}
        for _ in range(dictionary_size):
            key = self._deserialize(key_type_code)
            value = self._deserialize(value_type_code)
            dictionary[key] = value
        return dictionary

    def deserialize_hashtable(self):
        size = self.deserialize_short()
        hashtable = {}
        for _ in range(size):
            key = self.deserialize()
            value = self.deserialize()
            hashtable[key] = value
        return hashtable

    def deserialize_string_array(self):
        array_size = self.deserialize_short()
        array = []
        for _ in range(array_size):
            array.append(self.deserialize_string())
        return array

    def deserialize_byte_array(self):
        array_size = self.deserialize_integer()
        return self.read(array_size)

    def deserialize_object_array(self):
        array_size = self.deserialize_short()
        array = []
        for _ in range(array_size):
            array.append(self.deserialize())
        return array

    def deserialize_parameter_table(self):
        dictionary_size = self.deserialize_short()
        dictionary = {}
        for _ in range(dictionary_size):
            key = self.deserialize_byte()
            value_type_code = self.deserialize_byte()
            value = self._deserialize(value_type_code)
            dictionary[key] = value
        return dictionary

    def deserialize_event_data(self):
        code = self.deserialize_byte()
        parameters = self.deserialize_parameter_table()
        return {"type": "event", "code": code, "parameters": parameters}

    def deserialize_operation_request(self):
        code = self.deserialize_byte()
        parameters = self.deserialize_parameter_table()
        return {"type": "request", "code": code, "parameters": parameters}

    def deserialize_operation_response(self):
        code = self.deserialize_byte()
        return_code = self.deserialize_short()
        debug_message = self.deserialize_string() # Assuming string type code is read here
        parameters = self.deserialize_parameter_table()
        return {"type": "response", "code": code, "return_code": return_code, "debug_message": debug_message, "parameters": parameters}

    @staticmethod
    def parse_photon_message(payload):
        # The payload should start with the Photon header (0xF1, 0xF2, 0xFE) followed by the message type code
        # We need to skip the initial header bytes which are part of the Enet/Photon transport layer
        
        # Simple check for a known Photon header byte
        if not payload or payload[0] not in {0xF1, 0xF2, 0xFE}:
            return None

        # Determine the actual message start based on the C# code (which uses Protocol16Deserializer)
        # The C# code is called after the transport layer has been stripped.
        # For simplicity with Scapy, we'll assume the message type code is the first byte after the Enet/Photon header.
        
        # In the C# code, the deserializer is called with the raw payload *after* the Enet/Photon headers.
        # Based on the C# code, the first thing read is the message type code.
        
        # Let's try to find the message type code (which should be the first byte of the data to be deserialized)
        # For now, we'll skip the first byte (the header) and try to deserialize the rest.
        
        # This is a simplification, but necessary without full Enet/Photon protocol translation.
        
        try:
            parser = PhotonParser(payload[1:]) # Skip the first byte (Enet/Photon header)
            
            # The C# code reads the message type code first, then calls _deserialize(type_code).
            # The structure of the C# code suggests the message type (EventData, OpRequest, OpResponse) 
            # is implicitly known by the context where the deserializer is called.
            
            # Since we are interested in Events (UpdateMoney, CombatEvent), we will assume EventData (101)
            # is the expected type, or try to infer it.
            
            # Given the complexity, we'll try to find the type code in the payload.
            # A common pattern for Photon events is: [Header] [Type: EventData (101)] [Code] [Parameters]
            
            # Let's try to read the message type code (which should be the first byte of the data)
            message_type_code = payload[1] # Assuming the first byte after the header is the type code
            
            # Reset parser to the start of the message (after the header)
            parser = PhotonParser(payload[1:])
            
            # The C# deserializer is smart enough to read the type code if it's not provided, 
            # but here we are simplifying. Let's just try to deserialize the whole thing.
            
            # The C# code is: Deserialize(input, (byte) input.ReadByte());
            # This means the first byte of the stream is the type code.
            
            # Let's assume the payload is the raw Photon message:
            parser = PhotonParser(payload)
            
            # Try to read the message type code
            message_type_code = parser.deserialize_byte()
            
            # Reset parser for full deserialization
            parser = PhotonParser(payload)
            
            # The C# code is: Deserialize(input, (byte) input.ReadByte());
            # This is a recursive call. Let's simplify and assume the payload is the EventData structure.
            
            # We must find the correct starting point. Based on the C# code, the raw payload is passed to the parser.
            # Let's assume the payload is the raw Photon message, which starts with the message type code.
            
            # Try to deserialize as EventData, which is the most common for stats updates.
            # EventData structure: [EventCode (Byte)] [ParameterTable (Dictionary<Byte, Object>)]
            
            # We will use the C# logic for EventData:
            # 1. Read EventCode (Byte)
            # 2. Read ParameterTable (Dictionary<Byte, Object>)
            
            parser = PhotonParser(payload)
            code = parser.deserialize_byte()
            parameters = parser.deserialize_parameter_table()
            
            return {"type": "event", "code": code, "parameters": parameters}

        except Exception as e:
            logger.error(f"Error parsing Photon message: {e}")
            return None

# --- Constants and Configuration ---
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
        self.damage_meter = defaultdict(lambda: DamageMeterEntry("Unknown Player")) 

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

        # Simple check for a known Photon header byte
        if not payload or payload[0] not in PHOTON_HEADERS:
            return

        # --- ACTUAL PHOTON DECODING ---
        photon_message = PhotonParser.parse_photon_message(payload[1:]) # Skip Enet/Photon header
        
        if photon_message and photon_message["type"] == "event":
            self._handle_event(photon_message["code"], photon_message["parameters"])

    def _handle_event(self, event_code, parameters):
        # Based on C# EventCodes.cs and Handlers
        
        # EventCodes.UpdateMoney (86)
        if event_code == 86:
            # UpdateMoneyEvent: map[0:ObjectId, 1:CurrentSilver]
            if 1 in parameters:
                # The C# code uses FixPoint.FromInternalValue(parameters[1].ObjectToLong() ?? 0)
                # We assume the long value is the internal silver value
                silver_internal = parameters[1]
                # Since we don't have the FixPoint class, we'll assume the value is directly usable or needs simple conversion
                # The C# code suggests a long value. Let's use it directly for now.
                self.stats_model.silver_gained = silver_internal
                self.stats_model.add_notification(f"Silver updated: {silver_internal}", "silver")
                logger.info(f"UpdateMoney: {silver_internal}")
                
        # EventCodes.UpdateFame (87)
        elif event_code == 87:
            # UpdateFame: map[0:ObjectId, 1:TotalPlayerFame, ...]
            if 1 in parameters:
                fame_internal = parameters[1]
                self.stats_model.fame_gained = fame_internal
                self.stats_model.add_notification(f"Fame updated: {fame_internal}", "fame")
                logger.info(f"UpdateFame: {fame_internal}")
                
        # EventCodes.KilledPlayer (170) or Died (171) - For Damage Meter/Kills/Deaths
        # This is where the CombatController logic would be translated.
        elif event_code == 170:
            # KilledPlayer: map[0:killerId, 1:victimId, ...]
            self.stats_model.kills += 1
            self.stats_model.add_notification("Player Kill recorded", "kill")
            # Damage meter update logic based on parameters[0] (killer)
            
        elif event_code == 171:
            # Died: map[0:victimId, 1:killerId, ...]
            self.stats_model.deaths += 1
            self.stats_model.add_notification("Death recorded", "death")
            # Damage meter update logic based on parameters[0] (victim)
            
        # Placeholder for CombatEvent/Damage Meter logic
        # Since the C# code uses many specific event types (like CastHit, Attack), 
        # we'll keep the simulation for Damage Meter until the full combat logic is translated.
        # For now, we will use the Kill/Death events to update the count.
        
        # Fallback for Damage Meter (Simulation for UI demonstration)
        if event_code in {86, 87, 170, 171}:
            self._simulate_damage_meter_update(parameters)


    def _simulate_damage_meter_update(self, parameters):
        # SIMULATION: Damage Meter update logic for UI demonstration
        # In a real scenario, this would be updated by CastHit, Attack, etc. events.
        if 1 in parameters:
            player_id = parameters[1] % 3 # Simulate 3 players
            player_name = f"Player {player_id}"
            
            entry = self.stats_model.damage_meter[player_name]
            entry.player_name = player_name 
            
            # Simulate damage done and healing done
            damage_amount = (parameters[1] % 1000) + 500
            healing_amount = (parameters[1] % 500) + 100
            
            if self.stats_model.get_time_elapsed() % 2 == 0:
                entry.update_damage_done(damage_amount)
                self.stats_model.add_notification(f"{player_name} dealt {damage_amount} damage (Simulated)", "damage")
            else:
                entry.update_healing_done(healing_amount)
                self.stats_model.add_notification(f"{player_name} healed {healing_amount} (Simulated)", "healing")

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
            if self.is_tracking and self.page:
                self._update_dashboard_tab()
                self._update_damage_meter_tab()
                self._update_notifications()
                try:
                    self.page.update()
                except Exception as e:
                    # Catch update errors when app is closing
                    logger.debug(f"Flet update error: {e}")
                    pass
            time.sleep(0.5)

    def _update_dashboard_tab(self):
        elapsed_time = self.stats.get_time_elapsed()
        stats_per_hour = self.stats.get_stats_per_hour()
        
        self.silver_text.value = f"Silver: {self.stats.silver_gained:,}"
        self.fame_text.value = f"Fame: {self.stats.fame_gained:,}"
        self.kills_text.value = f"Kills: {self.stats.kills}"
        self.deaths_text.value = f"Deaths: {self.stats.deaths}"
        self.looted_chests_text.value = f"Looted Chests: {self.stats.looted_chests}"
        self.silver_per_hour_text.value = f"Silver/Hour: {stats_per_hour['silver']:,.0f}"
        self.fame_per_hour_text.value = f"Fame/Hour: {stats_per_hour['fame']:,.0f}"
        
        # Format time elapsed
        td = timedelta(seconds=int(elapsed_time))
        self.time_elapsed_text.value = f"Time: {str(td)}"

    def _update_damage_meter_tab(self):
        elapsed_time = self.stats.get_time_elapsed()
        sorted_entries = sorted(self.stats.damage_meter.values(), key=lambda x: x.damage_done, reverse=True)
        
        rows = []
        for entry in sorted_entries:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(entry.player_name)),
                        ft.DataCell(ft.Text(f"{entry.damage_done:,}")),
                        ft.DataCell(ft.Text(f"{entry.get_dps(elapsed_time):,.0f}")),
                        ft.DataCell(ft.Text(f"{entry.healing_done:,}")),
                    ]
                )
            )
        self.damage_meter_data_table.rows = rows

    def _update_notifications(self):
        # Update only if there are new notifications
        if len(self.notifications_list.controls) != len(self.stats.notifications):
            self.notifications_list.controls.clear()
            for notif in reversed(self.stats.notifications):
                color = ft.Colors.BLUE_GREY_100
                if notif["type"] == "silver":
                    color = ft.Colors.AMBER_500
                elif notif["type"] == "kill":
                    color = ft.Colors.RED_500
                elif notif["type"] == "death":
                    color = ft.Colors.BLACK
                
                self.notifications_list.controls.append(
                    ft.Container(
                        content=ft.Text(f"[{notif['timestamp']}] {notif['message']}", size=10),
                        padding=5,
                        bgcolor=color,
                        border_radius=5
                    )
                )

    def start_tracking_click(self, e):
        interface = self.interface_dropdown.value
        self.tracker.start_tracking(interface)
        self.is_tracking = True
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.status_text.value = f"Status: Tracking on {interface}"
        self.status_text.color = ft.Colors.GREEN_500
        self.page.snack_bar.content = ft.Text(f"Tracking started on {interface}. (Requires root/admin privileges)")
        self.page.snack_bar.open = True
        self.page.update()

    def stop_tracking_click(self, e):
        self.tracker.stop_tracking()
        self.is_tracking = False
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.status_text.value = "Status: Stopped"
        self.status_text.color = ft.Colors.RED_500
        self.page.snack_bar.content = ft.Text("Tracking stopped.")
        self.page.snack_bar.open = True
        self.page.update()

    def reset_stats_click(self, e):
        self.stats.reset()
        self.page.snack_bar.content = ft.Text("Statistics reset.")
        self.page.snack_bar.open = True
        self.page.update()

    def save_session_click(self, e):
        self.stats.save_to_file()
        self.page.snack_bar.content = ft.Text("Session saved successfully.")
        self.page.snack_bar.open = True
        self.page.update()

    def main(self, page: ft.Page):
        self.page = page
        page.title = "Albion Insight"
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.START
        page.window_width = 800
        page.window_height = 600
        page.snack_bar = ft.SnackBar(ft.Text("Welcome to Albion Insight!"))

        # Tabs Content
        dashboard_content = ft.Container(
            content=ft.Column(
                [
                    ft.Row([self.silver_text, self.fame_text, self.time_elapsed_text]),
                    ft.Row([self.kills_text, self.deaths_text, self.looted_chests_text]),
                    ft.Divider(),
                    ft.Row([self.silver_per_hour_text, self.fame_per_hour_text]),
                    ft.Divider(),
                    ft.Text("Notifications/Events:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Container(self.notifications_list, height=200, border=ft.border.all(1, ft.Colors.GREY_500), border_radius=5)
                ],
                scroll=ft.ScrollMode.ADAPTIVE
            ),
            padding=10
        )

        damage_meter_content = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Damage Meter (Simulated):", size=18, weight=ft.FontWeight.BOLD),
                    ft.Container(self.damage_meter_data_table, expand=True, padding=ft.padding.only(top=10))
                ],
                expand=True
            ),
            padding=10
        )

        # Main Layout
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                self.interface_dropdown,
                                self.start_button,
                                self.stop_button,
                                self.reset_button,
                                self.save_button,
                                ft.Container(self.status_text, alignment=ft.alignment.center_right, expand=True)
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                        ft.Tabs(
                            selected_index=0,
                            animation_duration=300,
                            expand=True,
                            tabs=[
                                ft.Tab(
                                    text="Dashboard",
                                    icon=ft.Icons.DASHBOARD,
                                    content=dashboard_content
                                ),
                                ft.Tab(
                                    text="Damage Meter",
                                    icon=ft.icons.SWORDS,
                                    content=damage_meter_content
                                ),
                                # Add other tabs here (e.g., Gathering, Trade, Settings)
                            ],
                        ),
                    ],
                    expand=True
                ),
                padding=10
            )
        )

        # Initial UI update
        self._update_dashboard_tab()
        self._update_damage_meter_tab()
        page.update()

# --- Application Entry Point ---
if __name__ == "__main__":
    # Check for root/admin privileges (simplified check for Linux)
    if os.name != 'nt' and os.geteuid() != 0:
        logger.warning("Application should be run with root privileges for network sniffing.")
        # Continue running the app, but inform the user.
        
    # The PhotonParser logic is now included and used in NetworkTracker._process_packet
    
    app = AlbionInsightApp()
    ft.app(target=app.main)

