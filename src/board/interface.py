from abc import ABC, abstractmethod

from app.utils import ui_setup


class Board(ABC):
    """
    This is the interface for board in games
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def interact(self, *args, **kwargs):
        """
        This method is to be used to interact with the board
        """
        pass

    @abstractmethod
    def reset(self, *args, **kwargs):
        """
        This method is to be used to reset the board to it's state at the beginning of a game
        """
        pass

    def get_params(self) -> dict:
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
        params = self.get_params()  # get the initialization parameters
        if params:
            new_params = ui_setup(params, 'Board')  # create the pop up and get the new parameters
            self.__init__(**new_params)  # reinitialize the object
