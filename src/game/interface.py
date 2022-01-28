from abc import ABC, abstractmethod
from typing import List

from src.player.interface import Player


class Game(ABC):
    players: List[Player] = []
    current_player: int = None

    def set_up(self, *args, **kwargs):
        pass

    def add_player(self, *args, **kwargs):
        pass

    def remove_player(self, *args, **kwargs):
        pass

    def end_condition(self, *args, **kwargs):
        pass

    def play(self, *args, **kwargs):
        pass

    def update_turn(self, *args, **kwargs):
        pass

    def get_winner(self, *args, **kwargs):
        pass
