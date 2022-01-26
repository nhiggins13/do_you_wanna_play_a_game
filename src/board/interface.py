from abc import ABC, abstractmethod


class Board(ABC):

    @abstractmethod
    def initialize(self, *args, **kwargs):
        pass
