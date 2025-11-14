from dataclasses import dataclass, field
from typing import Dict


@dataclass
class PlayerStats:
    """
    Modelo de dados para armazenar as estatísticas de um jogador.
    """

    name: str
    silver: int = 0
    fame: int = 0
    damage_done: int = 0
    healing_done: int = 0
    kills: int = 0
    deaths: int = 0


@dataclass
class SessionStats:
    """
    Modelo de dados para armazenar as estatísticas da sessão atual.
    """

    start_time: float = field(default_factory=lambda: 0.0)
    end_time: float = field(default_factory=lambda: 0.0)
    total_silver: int = 0
    total_fame: int = 0
    players: Dict[str, PlayerStats] = field(default_factory=dict)


@dataclass
class CombatEvent:
    """
    Modelo de dados para um evento de combate (ex: dano, cura).
    """

    event_type: str
    source_player: str
    target_player: str
    value: int
    timestamp: float
