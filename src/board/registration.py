from src.board.interface import Board
from collections import deque
from numpy.random import RandomState
from common.utils import register
from common.factory import BoardFactory


@register('ChainBoard', BoardFactory)
class ChainBoard(Board):
    values: deque = None
    seed = None
    random_state = None

    def __init__(self, length=5, seed=None, minimum=-100, maximum=100):
        self.initialize(length, seed, minimum, maximum)

    def initialize(self, length=5, seed=None, minimum=-100, maximum=100):
        self.min = minimum
        self.max = maximum
        self.seed = seed
        self.random_state = RandomState(seed)
        self.values = deque([self.random_state.randint(minimum, maximum) for _ in range(length)])

    def interact(self, side):
        if side not in ('L', 'R'):
            raise ValueError('Input must be "L" or "R", % was given' % side)

        if side == 'L':
            return self.values.popleft()

        return self.values.pop()

    def reset(self):
        self.initialize(length=len(self.values), seed=self.seed, minimum=self.min, maximum=self.max)
