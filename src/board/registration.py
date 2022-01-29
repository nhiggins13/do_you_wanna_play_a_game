import time

from board.interface import Board
from collections import deque
from numpy.random import RandomState
from common.utils import register
from common.factory import BoardFactory


@register('ChainBoard', BoardFactory)
class ChainBoard(Board):
    """
    This class implements the base chain game board
    """
    values: deque = None
    seed = None
    random_state = None

    def __init__(self, seed=None, minimum=-100, maximum=100):
        """
        set up the board
        :param seed: random seed so the same game can be replayed
        :param minimum: minimum value in the chain
        :param maximum: maximum value in the chain
        """
        self.min = minimum
        self.max = maximum
        self.seed = int(time.time()) if seed is None else seed
        self._create_values() # create the chain

    def _create_values(self):
        """
        sets the random state and creates a chain
        :return:
        """
        self.random_state = RandomState(self.seed)
        self.values = deque(
            [self.random_state.randint(self.min, self.max) for _ in range(self.random_state.randint(5, 100))])

    def interact(self, side) -> int:
        """
        pop a value from the chain
        :param side: the side the value will be popped from
        :return: the poppeed value
        """

        # raise and error if the values are not L or R
        if side not in ('L', 'R'):
            raise ValueError('Input must be "L" or "R", % was given' % side)

        if side == 'L':  # pop from left and return
            return self.values.popleft()

        return self.values.pop()  # pop from right and return

    def reset(self):
        """
        reset the random state and chain
        :return:
        """
        self._create_values()

    def get_params(self) -> dict:
        """
        get the initialization parameters and return a dictionary of them
        :return: dictionary key: parameter name, value (current value, description, type)
        """
        params = super().get_params()
        params['minimum'] = (self.min, 'Minimum value in chain', int)
        params['maximum'] = (self.max, 'Maximum value in chain', int)
        params['seed'] = (self.seed, 'Random seed', int)

        return params

