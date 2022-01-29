from abc import ABC, abstractmethod
from typing import List

from app.player_ui_setup import player_ui_setup
from src.player.interface import Player


class Game(ABC):
    players: List[Player] = []
    current_player: int = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_player(self, *args, **kwargs):
        pass

    @abstractmethod
    def remove_player(self, *args, **kwargs):
        pass

    @abstractmethod
    def end_condition(self, *args, **kwargs):
        pass

    @abstractmethod
    def play_turn(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_turn(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_winner(self, *args, **kwargs):
        pass

    def get_params(self):
        return {}

    def gui_setup(self):
        params = self.get_params()
        if params:
            new_params = player_ui_setup(params)
            self.__init__(**new_params)
