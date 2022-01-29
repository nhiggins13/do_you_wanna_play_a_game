import unittest
from collections import deque

from board.registration import ChainBoard


class TestChainBoard(unittest.TestCase):
    def setUp(self):
        self.board_cls = ChainBoard
        self.kwargs = dict(seed=123)

    def test_init(self):
        target_values = deque([-2, -83, -17, 6, 23, -43, -4, 13, 26, -53, -27, -68, 74, 11, 53, -17, -22, 64, -4, -32,
                               -51, -45, 95, -98, -16, -61, -34, -16, -53, 89, 76, 35, 5, -1, 24, -8, 80, 2, -3, 18, -6,
                               55, -66, -24, 68, 31, 6, -31, -36, -25, 62, -42, 38, -78, 46, -85, 55, 58, 80, -30, 9,
                               15, 54, 34, -86, 3, 82, 99, 29, -57, 86])

        board = self.board_cls(**self.kwargs)
        assert target_values == board.values

    def test_interact(self):
        board = self.board_cls(**self.kwargs)
        left = board.values[0]
        right = board.values[-1]

        assert left == board.interact('L')
        assert right == board.interact('R')

    def test_reset(self):
        board = self.board_cls(**self.kwargs)
        target = board.values.copy()
        board.values = [1, 2, 3, 4, 5]
        board.reset()
        assert target == board.values

    def test_get_params(self):
        board = self.board_cls(**self.kwargs)
        params = board.get_params()
        assert params == {'minimum': (-100, 'Minimum value in chain', int),
                          'maximum': (100, 'Maximum value in chain', int),
                          'seed': (123, 'Random seed', int)}