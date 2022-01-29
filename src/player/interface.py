from abc import ABC, abstractmethod

from app.player_ui_setup import player_ui_setup


class Player(ABC):

    score = 0.0
    is_bot: bool = True
    game: str = None
    name: str = 'Player'

    _idCounter = 0

    def __init__(self, name):
        if name:
            self.name = name
        else:
            name += str(self._idCounter)

    def reset(self):
        self.score = 0.0

    @abstractmethod
    def play_turn(self, *args, **kwargs):
        pass

    def get_params(self):
        return {'name': (self.name, 'Name of the Player', str)}

    def gui_setup(self):
        params = self.get_params()
        if len(params) > 1:
            new_params = player_ui_setup(params)
            self.__init__(**new_params)
