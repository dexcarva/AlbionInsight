from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)

class PlayerStats:
    """
    Encapsula as estatísticas de um jogador para o Damage Meter.
    """
    def __init__(self, name: str):
        self.name = name
        self.damage_done = 0.0
        self.healing_done = 0.0
        self.last_activity = datetime.now()

    def add_damage(self, amount: float):
        self.damage_done += amount
        self.last_activity = datetime.now()

    def add_healing(self, amount: float):
        self.healing_done += amount
        self.last_activity = datetime.now()

    def get_dps(self, session_duration_seconds: float) -> float:
        if session_duration_seconds > 0:
            return self.damage_done / session_duration_seconds
        return 0.0

    def to_dict(self, session_duration_seconds: float) -> dict:
        return {
            "name": self.name,
            "damage": int(self.damage_done),
            "dps": self.get_dps(session_duration_seconds),
            "healing": int(self.healing_done),
            "last_activity": self.last_activity.isoformat()
        }

class SessionStats:
    """
    Gerencia todas as estatísticas da sessão.
    """
    def __init__(self):
        # Map from object_id to PlayerStats instance
        self.players: dict[int, PlayerStats] = {} 
        # Map from object_id to player_name (for quick lookup)
        self.player_id_map: dict[int, str] = {} 
        self.start_time: datetime | None = None
        self.is_running = False

    def start(self):
        self.start_time = datetime.now()
        self.is_running = True

    def stop(self):
        self.is_running = False

    def reset(self):
        self.players.clear()
        self.player_id_map.clear()
        self.start_time = datetime.now() if self.is_running else None
        logger.info("Session data reset.")

    def get_duration_seconds(self) -> float:
        if self.start_time and self.is_running:
            return (datetime.now() - self.start_time).total_seconds()
        return 0.0

    def get_session_duration_formatted(self):
        '''Returns the current session duration as a formatted string.'''
        if not self.start_time or not self.is_running:
            return "00:00:00"
        
        duration = datetime.now() - self.start_time
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def get_player_stats(self, object_id: int, player_name: str | None = None) -> PlayerStats:
        if object_id not in self.players:
            if player_name is None:
                # Fallback to a generic name if ID is not mapped yet
                player_name = f"Unknown Player {object_id}"
            
            self.players[object_id] = PlayerStats(player_name)
            self.player_id_map[object_id] = player_name
            
        return self.players[object_id]

    def get_damage_meter_data(self) -> list[dict]:
        duration = self.get_duration_seconds()
        data = [stats.to_dict(duration) for stats in self.players.values()]
        
        # Sort by damage done (descending)
        data.sort(key=lambda x: x["damage"], reverse=True)
        return data

    def save_session(self):
        '''Saves the current session data to a JSON file.'''
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"albion_insight_session_{timestamp}.json"
        
        # Prepare data for serialization
        players_data = {
            stats.name: {
                "damage_done": stats.damage_done,
                "healing_done": stats.healing_done,
                "last_activity": stats.last_activity.isoformat()
            } for stats in self.players.values()
        }

        session_data = {
            "timestamp": timestamp,
            "duration": self.get_session_duration_formatted(),
            "players": players_data,
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
