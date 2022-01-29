from abc import ABC, abstractmethod
from typing import List

from app.utils import ui_setup
from player.interface import Player


class Game(ABC):
    """
    Interface for games
    """
    players: List[Player] = []
    current_player: int = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_player(self, *args, **kwargs):
        """Adds player to the game"""
        pass

    @abstractmethod
    def remove_player(self, *args, **kwargs):
        """Remove player from game"""
        pass

    @abstractmethod
    def end_condition(self, *args, **kwargs) -> bool:
        """returns True if end condition is met"""
        pass

    @abstractmethod
    def play_turn(self, *args, **kwargs):
        """plays a turn of the game"""
        pass

    @abstractmethod
    def update_turn(self, *args, **kwargs):
        """updates whos turn it is"""
        pass

    @abstractmethod
    def get_winner(self, *args, **kwargs) -> List[Player]:
        """
        returns a list of winners
        :param args:
        :param kwargs:
        :return: a list of player objects
        """
        pass

    def get_scores(self) -> List[int]:
        """
        returns a list of player scores
        :return: a list of player scores
        """
        return [p.score for p in self.players]

    def get_params(self):
        """
        This method returns the initialization parameters of the board
        :return: a dictionary of the initialization parameters of the board
        """
        return {}

    def gui_setup(self):
        """
        This method get's the initialization parameters and creates a popup with them and then reinitializes the object
        from the user inputs
        :return:
        """
        params = self.get_params()
        if params:
            new_params = ui_setup(params, 'Game')
            self.__init__(**new_params)
