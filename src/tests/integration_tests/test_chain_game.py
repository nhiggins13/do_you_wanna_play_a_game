import unittest

from board.registration import ChainBoard
from game.registration import ChainGame
from player.registration import OneSidedChainBot, GreedyChainBot


class TestChainGame(unittest.TestCase):
    def setUp(self):
        self.players = [OneSidedChainBot(name='Lefty', side='L'), GreedyChainBot(name='Greedy')]

    def test_game(self):

        # play 100 games and check that the results are the same
        for i in range(100):
            self.board = ChainBoard(seed=i)
            game = ChainGame(players=self.players, board=self.board)
            while game.end_condition():
                game.play_turn()

            winners = [p.name for p in game.get_winner()]

            if i == 0:
                assert winners == ['Lefty']
            else:
                assert winners == ['Greedy']
