from abc import ABC, abstractmethod


class Board(ABC):

    @abstractmethod
    def initialize(self, *args, **kwargs):
        pass

    @abstractmethod
    def interact(self, *args, **kwargs):
        pass

    @abstractmethod
    def reset(self, *args, **kwargs):
        pass
