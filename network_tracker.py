'''
Network tracking and Photon protocol decoding logic for Albion Insight.
'''
import logging
import struct
import threading
import time
from enum import Enum
from scapy.all import sniff, UDP, IP, get_if_list
from collections import defaultdict
from datetime import datetime, timedelta

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
        # The C# code reads a string here, which is the debug message.
        # In Python, we need to read the type code first, then the value.
        # Assuming the debug message is always a string (type code 115)
        debug_message_type = self.deserialize_byte()
        if debug_message_type == Protocol16Type.String.value:
            debug_message = self.deserialize_string()
        else:
            # Fallback if it's not a string, though unlikely for debug message
            debug_message = self._deserialize(debug_message_type)
            logger.warning(f"Debug message was not a string (type {debug_message_type})")

        parameters = self.deserialize_parameter_table()
        return {"type": "response", "code": code, "return_code": return_code, "debug_message": debug_message, "parameters": parameters}

    @staticmethod
    def parse_photon_message(payload):
        # Simplified Enet/Photon header check and stripping
        if not payload or payload[0] not in {0xF1, 0xF2, 0xFE}:
            return None

        # The actual Photon message starts after the Enet/Photon header (usually 1 byte)
        try:
            parser = PhotonParser(payload[1:])
            
            # The first byte of the raw Photon message is the message type code
            message_type_code = parser.deserialize_byte()
            
            # Reset parser to the start of the message (after the header)
            parser = PhotonParser(payload[1:])
            
            # The C# code calls Deserialize(input, (byte) input.ReadByte());
            # which means it reads the type code and then calls the internal deserializer.
            # We need to read the type code again and pass it to _deserialize.
            
            # Read the type code again
            type_code = parser.deserialize_byte()
            
            # Now deserialize the content based on the type code
            return parser._deserialize(type_code)

        except Exception as e:
            logger.error(f"Error parsing Photon message: {e}")
            return None

        except Exception as e:
            logger.error(f"Error during sniffing: {e}")
            self.is_running = False
            self.update_callback() # Notify UI of error

    def _process_packet(self, packet):
        if not self.is_running:
            return

        if IP in packet and UDP in packet:
            payload = bytes(packet[UDP].payload)
            
            # The payload is the raw Enet/Photon message
            parsed_message = PhotonParser.parse_photon_message(payload)
            
            if parsed_message and parsed_message.get("type") == "event":
                self._handle_event(parsed_message)

    def _handle_event(self, event):
        event_code = event["code"]
        params = event["parameters"]
        
        # Event Codes (Simplified from C# project)
        # 1: UpdateMoney
        # 2: UpdateFame
        # 3: KilledPlayer
        # 4: Died
        # 5: CombatEvent (This is the most complex one)
        
        if event_code == 5: # CombatEvent
            self._handle_combat_event(params)
        elif event_code == 1: # UpdateMoney
            # Not directly relevant for damage meter, but good for general stats
            pass
        elif event_code == 2: # UpdateFame
            pass
        elif event_code == 3: # KilledPlayer
            pass
        elif event_code == 4: # Died
            pass
        elif event_code == 10: # NewPlayer (Simplified, actual code is complex)
            # Example: {1: object_id, 2: player_name}
            object_id = params.get(1)
            player_name = params.get(2)
            if object_id and player_name:
                self.player_id_map[object_id] = player_name
                self.players[player_name]["name"] = player_name
                logger.info(f"New Player: {player_name} (ID: {object_id})")
        
        # After handling the event, notify the UI to update
        self.update_callback()

    def _handle_combat_event(self, params):
        # CombatEvent parameters (Simplified)
        # 0: EventType (Byte) - 1: Damage, 2: Healing
        # 1: SourceId (Integer) - ID of the entity that caused the damage/healing
        # 2: TargetId (Integer) - ID of the entity that received the damage/healing
        # 3: Amount (Float) - The amount of damage/healing
        
        event_type = params.get(0)
        source_id = params.get(1)
        amount = params.get(3)
        
        if not source_id or not amount:
            return

        source_name = self.player_id_map.get(source_id)
        
        if source_name:
            if event_type == 1: # Damage
                self.players[source_name]["damage_done"] += amount
                logger.debug(f"Damage: {source_name} hit for {amount}")
            elif event_type == 2: # Healing
                self.players[source_name]["healing_done"] += amount
                logger.debug(f"Healing: {source_name} healed for {amount}")

    def get_damage_meter_data(self):
        '''Returns data for the damage meter UI.'''
        data = []
        session_duration = (datetime.now() - self.start_time).total_seconds() if self.start_time and self.is_running else 0
        
        for name, stats in self.players.items():
            damage = int(stats["damage_done"])
            healing = int(stats["healing_done"])
            dps = damage / session_duration if session_duration > 0 else 0
            
            data.append({
                "name": name,
                "damage": damage,
                "dps": dps,
                "healing": healing
            })
            
        # Sort by damage done (descending)
        data.sort(key=lambda x: x["damage"], reverse=True)
        return data

    def get_session_duration(self):
        '''Returns the current session duration as a formatted string.'''
        if not self.start_time or not self.is_running:
            return "00:00:00"
        
        duration = datetime.now() - self.start_time
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def reset_session(self):
        '''Resets all session data.'''
        self.players.clear()
        self.player_id_map.clear()
        self.start_time = datetime.now() if self.is_running else None
        self.update_callback()
        logger.info("Session data reset.")

    def save_session(self):
        '''Saves the current session data to a JSON file.'''
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"albion_insight_session_{timestamp}.json"
        
        session_data = {
            "timestamp": timestamp,
            "duration": self.get_session_duration(),
            "players": dict(self.players),
            "player_id_map": self.player_id_map
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(session_data, f, indent=4)
            logger.info(f"Session saved to {filename}")
            return filename
        except Exception as e:
            logger.error(f"Error saving session: {e}")
            return None

# Set up basic logging for this module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
