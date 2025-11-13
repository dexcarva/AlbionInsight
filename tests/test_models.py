"""
Testes unitários para os modelos de dados do Albion Insight.
"""

import pytest
from albion_insight.core.models import PlayerStats, SessionStats, CombatEvent
import time


class TestPlayerStats:
    """Testes para a classe PlayerStats."""

    def test_player_stats_creation(self):
        """Testa a criação de uma instância de PlayerStats."""
        player = PlayerStats(name="TestPlayer")
        assert player.name == "TestPlayer"
        assert player.silver == 0
        assert player.fame == 0
        assert player.damage_done == 0
        assert player.healing_done == 0
        assert player.kills == 0
        assert player.deaths == 0

    def test_player_stats_with_values(self):
        """Testa a criação de PlayerStats com valores iniciais."""
        player = PlayerStats(
            name="TestPlayer",
            silver=1000,
            fame=500,
            damage_done=100,
            healing_done=50,
            kills=5,
            deaths=2,
        )
        assert player.silver == 1000
        assert player.fame == 500
        assert player.damage_done == 100
        assert player.healing_done == 50
        assert player.kills == 5
        assert player.deaths == 2


class TestSessionStats:
    """Testes para a classe SessionStats."""

    def test_session_stats_creation(self):
        """Testa a criação de uma instância de SessionStats."""
        session = SessionStats()
        assert session.start_time == 0.0
        assert session.end_time == 0.0
        assert session.total_silver == 0
        assert session.total_fame == 0
        assert session.players == {}

    def test_session_stats_with_players(self):
        """Testa a adição de jogadores a uma sessão."""
        session = SessionStats()
        player1 = PlayerStats(name="Player1", silver=1000)
        player2 = PlayerStats(name="Player2", silver=2000)

        session.players["Player1"] = player1
        session.players["Player2"] = player2

        assert len(session.players) == 2
        assert session.players["Player1"].silver == 1000
        assert session.players["Player2"].silver == 2000


class TestCombatEvent:
    """Testes para a classe CombatEvent."""

    def test_combat_event_creation(self):
        """Testa a criação de uma instância de CombatEvent."""
        current_time = time.time()
        event = CombatEvent(
            event_type="damage",
            source_player="Player1",
            target_player="Player2",
            value=100,
            timestamp=current_time,
        )

        assert event.event_type == "damage"
        assert event.source_player == "Player1"
        assert event.target_player == "Player2"
        assert event.value == 100
        assert event.timestamp == current_time

    def test_combat_event_healing(self):
        """Testa a criação de um evento de cura."""
        current_time = time.time()
        event = CombatEvent(
            event_type="healing",
            source_player="Healer",
            target_player="Player1",
            value=50,
            timestamp=current_time,
        )

        assert event.event_type == "healing"
        assert event.value == 50
