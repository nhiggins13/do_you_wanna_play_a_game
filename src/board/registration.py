import time

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

    def __init__(self, seed=None, minimum=-100, maximum=100):
        self.min = minimum
        self.max = maximum
        self.seed = int(time.time()) if seed is None else seed
        self.random_state = RandomState(self.seed)
        self.values = deque([self.random_state.randint(minimum, maximum) for _ in range(self.random_state.randint(5, 100))])

    def interact(self, side):
        if side not in ('L', 'R'):
            raise ValueError('Input must be "L" or "R", % was given' % side)

        if side == 'L':
            return self.values.popleft()

        return self.values.pop()

    def reset(self):
        self.random_state = RandomState(self.seed)
        self.values = deque([self.random_state.randint(self.min, self.max) for _ in range(self.length)])

    def get_params(self):
        params = super().get_params()
        params['minimum'] = (self.min, 'Minimum value in chain', int)
        params['maximum'] = (self.max, 'Maximum value in chain', int)
        params['seed'] = (self.seed, 'Random seed', int)

        return params

