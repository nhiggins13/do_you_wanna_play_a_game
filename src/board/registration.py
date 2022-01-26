from src.board.interface import Board
from collections import deque
import random


class ChainBoard(Board):
    values: deque = None

    def initialize(self, length=5, seed=None, minimum=-100, maximum=100):
        random.seed(seed)
        self.values = deque([random.randint(minimum, maximum) for _ in range(length)])
