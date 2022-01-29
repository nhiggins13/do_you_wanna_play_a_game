import unittest
from collections import deque
from copy import copy
from random import random

from board.registration import ChainBoard
from player.registration import HumanChainPlayer, OneSidedChainBot, GreedyChainBot, RandomChainBot


class TestPlayer(unittest.TestCase):
    player_cls = HumanChainPlayer

    def setUp(self):
        self.args = []
        self.kwargs = {'name': 'test'}
        self.params = {'name': (self.kwargs['name'], 'Name of the Player', str)}

    def test_init(self):
        player = self.player_cls(*self.args, **self.kwargs)
        assert player.name == self.kwargs['name']
        player = self.player_cls()
        last_unique_id = player.name.split('_')[1]
        player = self.player_cls()
        assert 'Player_' + str(int(last_unique_id)+1) == 'Player_1'

    def test_reset(self):
        player = self.player_cls(*self.args, **self.kwargs)
        player.score = 100
        player.reset()
        assert player.score == 0.0

    def test_get_params(self):
        player = self.player_cls(*self.args, **self.kwargs)
        assert player.get_params() == self.params


class TestOneSided(TestPlayer):
    player_cls = OneSidedChainBot

    def setUp(self):
        self.args = []
        self.kwargs = {'name': 'test', 'side': 'R'}
        self.params = {'name': (self.kwargs['name'], 'Name of the Player', str),
                       'side': (self.kwargs['side'], 'Side the bot chooses L or R', str)}

    def test_init(self):
        super().test_init()
        player = self.player_cls(*self.args, **self.kwargs)
        assert player.side == self.kwargs['side']

    def test_play_turn(self):

        values = [random() for _ in range(100)]
        player = self.player_cls(*self.args, **self.kwargs)
        for val in values:
            assert player.play_turn() == self.kwargs['side']


class TestGreedy(TestPlayer):
    player_cls = GreedyChainBot

    def test_play(self):
        targets = ['R', 'L', 'L', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'R', 'L', 'R', 'L', 'L', 'L',
                   'R', 'L', 'L', 'L', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'L',
                   'L', 'R', 'L', 'L', 'L', 'L', 'R', 'L', 'R', 'L', 'L', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'R', 'L',
                   'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']

        player = self.player_cls(*self.args, **self.kwargs)
        board = ChainBoard(seed=123)

        i = 0
        while board.values:
            result = player.play_turn(board=board)
            board.values.pop()
            assert result == targets[i]
            i += 1


class TestRandom(TestPlayer):
    player_cls = RandomChainBot

    def setUp(self):
        self.args = []
        self.kwargs = {'name': 'test', 'seed': 123}
        self.params = {'name': (self.kwargs['name'], 'Name of the Player', str),
                       'seed': (self.kwargs['seed'], 'Random seed', int)}

    def test_init(self):
        super().test_init()
        player = self.player_cls(*self.args, **self.kwargs)
        assert player.seed == self.kwargs['seed']

    def test_reset(self):
        player = self.player_cls(*self.args, **self.kwargs)
        targets = [player.random_state.randint(1,10) for _ in range(100)]
        player.reset()
        results = [player.random_state.randint(1,10) for _ in range(100)]
        assert targets == results

    def test_play_turn(self):
        targets = ['L', 'L', 'R', 'L', 'L', 'R', 'R', 'L', 'L', 'L', 'R', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'L', 'L',
                   'R', 'L', 'L', 'L', 'R', 'L', 'L', 'R', 'L', 'R', 'R', 'L', 'L', 'R', 'L', 'R', 'R', 'L', 'L', 'R',
                   'L', 'R', 'L', 'L', 'R', 'L', 'L', 'L', 'R', 'L', 'L', 'R', 'L', 'R', 'R', 'R', 'L', 'R', 'R', 'R',
                   'L', 'L', 'R', 'L', 'L', 'L', 'L', 'L', 'R', 'R', 'L', 'R', 'L', 'R', 'L', 'L', 'R', 'R', 'R', 'R',
                   'L', 'L', 'L', 'L', 'R', 'R', 'R', 'R', 'R', 'L', 'R', 'R', 'R', 'R', 'L', 'L', 'L', 'L', 'L', 'L']

        player = self.player_cls(*self.args, **self.kwargs)
        for i in range(100):
            result = player.play_turn()
            assert result == targets[i]

        print('done')

