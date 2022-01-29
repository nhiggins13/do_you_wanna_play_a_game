import unittest
from copy import copy

from board.registration import ChainBoard
from game.registration import ChainGame
from player.registration import RandomChainBot


class TestGame(unittest.TestCase):
    player_cls = ChainGame

    def test_init(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)
        assert game.current_player == 0

    def test_check_unique_player_names(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)
        assert game._check_unique_player_names(players)
        not_unique = [RandomChainBot(name=1, seed=1), RandomChainBot(name=1, seed=2)]
        assert not game._check_unique_player_names(not_unique)

    def test_add_player(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        player = RandomChainBot(name='tes', seed=123)
        game.add_player(player)
        assert game.players[-1] == player
        assert player.name in game.player_names

    def test_remove_player(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        player = copy(players[-1])
        assert player.name in game.player_names
        game.remove_player(player.name)
        assert player.name not in game.player_names
        for p in game.players:
            assert player.name != p.name

    def test_end_condition(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        assert not game.end_condition()
        board.values = []
        assert game.end_condition()

    def test_update_turn(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)
        assert game.current_player == 0
        game.update_turn()
        assert game.current_player == 1
        game.update_turn()
        assert  game.current_player == 0

    def test_play_turn(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        game.play_turn()
        assert game.current_player == 1
        assert players[0].score == 86
        assert board.values[-1] == -57

    def test_get_winners(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        assert game.get_winner() == players
        players[0].score = 100
        assert game.get_winner() == [players[0]]

    def test_reset(self):
        board = ChainBoard(seed=123)
        orig_values = board.values.copy()
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        for p in players:
            p.score = 100

        board.values = []
        game.current_player = 1

        game.reset_game()
        assert board.values == orig_values
        assert game.current_player == 0
        for p in players:
            assert p.score == 0

    def test_get_params(self):
        board = ChainBoard(seed=123)
        players = [RandomChainBot(name=1, seed=1), RandomChainBot(name=2, seed=2)]
        game = ChainGame(players, board)

        assert game.get_params() == {}