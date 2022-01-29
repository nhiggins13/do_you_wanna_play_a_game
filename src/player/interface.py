from abc import ABC, abstractmethod
from typing import Any

from app.utils import ui_setup


class Player(ABC):
    """
    Interface for players
    """

    score = 0.0
    is_bot: bool = True  # is the player a bot
    game: str = None  # the game this player plays
    name: str = 'Player'

    _idCounter = 0

    def __init__(self, name=None):
        # set the name and create unique name if default is used
        if name:
            self.name = name
        else:
            self.name = Player.unique_name()

    @classmethod
    def unique_name(cls):
        new_name = cls.name + '_' + str(cls._idCounter)
        cls._idCounter += 1
        return new_name

    def reset(self):
        """
        reset the player
        :return:
        """
        self.score = 0.0

    @abstractmethod
    def play_turn(self, *args, **kwargs) -> Any:
        """
        player makes his turn and returns their decision
        :param args:
        :param kwargs:
        :return: the players decision
        """
        pass

    def get_params(self):
        """
        This method returns the initialization parameters of the board
        :return: a dictionary of the initialization parameters of the board
        """
        return {'name': (self.name, 'Name of the Player', str)}

    def gui_setup(self):
        """
        This method get's the initialization parameters and creates a popup with them and then reinitializes the object
        from the user inputs
        :return:
        """
        params = self.get_params()
        if len(params) > 1:
            new_params = ui_setup(params, 'Player')
            self.__init__(**new_params)
