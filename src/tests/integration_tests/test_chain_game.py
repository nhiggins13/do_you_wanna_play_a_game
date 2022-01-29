import unittest

from board.registration import ChainBoard
from game.registration import ChainGame
from player.registration import OneSidedChainBot, GreedyChainBot


class TestChainGame(unittest.TestCase):
    def setUp(self):
        self.players = [GreedyChainBot(name='Greedy1'), GreedyChainBot(name='Greedy2')]

    def test_game(self):
        targets = [['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'],
                   ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'],
                   ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'],
                   ['Greedy1'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'],
                   ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy2'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'], ['Greedy1'],
                   ['Greedy1'], ['Greedy1']]


        # play 100 games and check that the results are the same
        for i in range(100):
            self.board = ChainBoard(seed=i)
            game = ChainGame(players=self.players, board=self.board)
            while not game.end_condition():
                game.play_turn()

            winners = [p.name for p in game.get_winner()]
            assert winners == targets[i]
