from abc import ABC, abstractmethod

from app.player_ui_setup import player_ui_setup


class Board(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def interact(self, *args, **kwargs):
        pass

    @abstractmethod
    def reset(self, *args, **kwargs):
        pass

    def get_params(self):
        return {}

    def gui_setup(self):
        params = self.get_params()
        if params:
            new_params = player_ui_setup(params)
            self.__init__(**new_params)