'''
Data models for Albion Insight.
'''
import flet as ft

class Player:
    '''Represents a player in the game.'''
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.damage_done = 0
        self.healing_done = 0

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
