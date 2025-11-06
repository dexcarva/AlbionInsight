'''
Network tracking and Photon protocol decoding logic for Albion Insight.
'''
import logging
import struct
import threading
import time
from enum import Enum
from scapy.all import sniff, UDP, IP, get_if_list
from datetime import datetime, timedelta
from models import SessionStats

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
            # Handle the case where the key or value deserialization failed
            if key is None or value is None:
                logger.warning("Failed to deserialize key or value in dictionary.")
                break
        return dictionary

    def deserialize_hashtable(self):
        size = self.deserialize_short()
        hashtable = {}
        for _ in range(size):
            key = self.deserialize()
            value = self.deserialize()
            hashtable[key] = value
            if key is None or value is None:
                logger.warning("Failed to deserialize key or value in hashtable.")
                break
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
            if key is None or value is None:
                logger.warning("Failed to deserialize key or value in parameter table.")
                break
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
        debug_message_type = self.deserialize_byte()
        if debug_message_type == Protocol16Type.String.value:
            debug_message = self.deserialize_string()
        else:
            debug_message = self._deserialize(debug_message_type)
            logger.warning(f"Debug message was not a string (type {debug_message_type})")

        parameters = self.deserialize_parameter_table()
        return {"type": "response", "code": code, "return_code": return_code, "debug_message": debug_message, "parameters": parameters}

    @staticmethod
    def parse_photon_message(payload):
        if not payload or payload[0] not in {0xF1, 0xF2, 0xFE}:
            return None

        try:
            parser = PhotonParser(payload[1:])
            type_code = parser.deserialize_byte()
            return parser._deserialize(type_code)

        except Exception as e:
            logger.error(f"Error parsing Photon message: {e}")
            return None

class NetworkTracker:
    def __init__(self, update_callback):
        self.update_callback = update_callback
        self.session_stats = SessionStats()
        self.sniff_thread = None

    def get_interfaces(self):
        return get_if_list()

    def start_sniffing(self, interface):
        if self.session_stats.is_running:
            return
        
        self.interface = interface
        self.session_stats.start()
        self.sniff_thread = threading.Thread(target=self._sniff_loop, daemon=True)
        self.sniff_thread.start()
        logger.info(f"Started sniffing on {interface}")

    def stop_sniffing(self):
        if not self.session_stats.is_running:
            return
        
        self.session_stats.stop()
        logger.info("Stopping sniffing...")

    def _sniff_loop(self):
        bpf_filter = "udp and (port 5055 or port 5056 or port 5058)"
        try:
            sniff(iface=self.interface, filter=bpf_filter, prn=self._process_packet, store=0, stop_filter=lambda x: not self.session_stats.is_running)
        except Exception as e:
            logger.error(f"Sniffing error: {e}")
        finally:
            self.session_stats.stop()
            logger.info("Sniffing thread finished.")

    def _process_packet(self, packet):
        if not self.session_stats.is_running:
            return

        if IP in packet and UDP in packet:
            payload = bytes(packet[UDP].payload)
            parsed_message = PhotonParser.parse_photon_message(payload)
            
            if parsed_message and parsed_message.get("type") == "event":
                self._handle_event(parsed_message)

    def _handle_event(self, event):
        event_code = event["code"]
        params = event["parameters"]
        
        if event_code == 5: # CombatEvent
            self._handle_combat_event(params)
        elif event_code == 10: # NewPlayer
            object_id = params.get(1)
            player_name = params.get(2)
            if object_id and player_name:
                self.session_stats.get_player_stats(object_id, player_name)
                logger.info(f"New Player: {player_name} (ID: {object_id})")
        
        self.update_callback()

    def _handle_combat_event(self, params):
        event_type = params.get(0)
        source_id = params.get(1)
        amount = params.get(3)
        
        if not source_id or not amount:
            return

        player_stats = self.session_stats.get_player_stats(source_id)
        
        if player_stats:
            if event_type == 1: # Damage
                player_stats.add_damage(amount)
                logger.debug(f"Damage: {player_stats.name} hit for {amount}")
            elif event_type == 2: # Healing
                player_stats.add_healing(amount)
                logger.debug(f"Healing: {player_stats.name} healed for {amount}")

    def get_damage_meter_data(self):
        return self.session_stats.get_damage_meter_data()

    def get_session_duration(self):
        return self.session_stats.get_session_duration_formatted()

    def reset_session(self):
        self.session_stats.reset()
        self.update_callback()

    def save_session(self):
        return self.session_stats.save_session()
