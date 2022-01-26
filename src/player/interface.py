from abc import ABC, abstractmethod


class Player(ABC):

    score = 0.0
    is_bot: bool = True
    game: str = None
    name: str = 'Player'

    _idCounter = 0

    def __init__(self, name, *args, **kwargs):
        if name:
            self.name = name
        else:
            name += str(self._idCounter)

    def reset_score(self, *args, **kwargs):
        self.score = 0

    @abstractmethod
    def play_turn(self, *args, **kwargs):
        pass