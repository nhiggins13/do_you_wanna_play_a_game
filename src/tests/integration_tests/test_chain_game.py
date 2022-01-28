import unittest

from game.registration import ChainGame
from player.registration import OneSidedChainBot, GreedyChainBot


class TestChainGame(unittest.TestCase):
    def setUp(self):
        self.players = [OneSidedChainBot(name='Lefty', side='L'), GreedyChainBot(name='Greedy')]
        self.game = ChainGame(players=self.players)


    def test_game(self):
        winners = self.game.play()
        assert winners[0].name == 'Greedy'