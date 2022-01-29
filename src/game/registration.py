from common.utils import register
from common.factory import GameFactory, BoardFactory
from game.interface import Game


@register('ChainGame', GameFactory)
class ChainGame(Game):
    player_names = set()
    board = None

    def __init__(self, players, board):
        self.current_player = 0
        if self._check_unique_player_names(players):
            self.players = players
            self.player_names = set(p.name for p in players)
        else:
            raise ValueError('Player names not unique')

        self.board = board

    def _check_unique_player_names(self, players):
        if isinstance(players, list):
            if len(players) == len(set(p.name for p in players)):
                return True
            return False
        elif players.name in self.player_names:
            return False

        return True

    def add_player(self, player):
        if player.name in self.player_names:
            raise ValueError('Player name %s already in the game' % player.name)

        self.players.append(player)
        self.player_names.add(player.name)

    def remove_player(self, player_name):
        if player_name in self.player_names:
            for i, p in enumerate(self.players):
                if p.name == player_name:
                    self.players.pop(i)
                    break

            self.player_names.remove(player_name)

    def end_condition(self):
        return True if self.board.values else False

    def play_turn(self):
        turn = self.players[self.current_player].play_turn(board=self.board)
        val = self.board.interact(side=turn)
        self.players[self.current_player].score += val
        self.update_turn()

    def update_turn(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def get_winner(self):
        scores = sorted(self.players, key=lambda p: -p.score)
        winners = [scores[0]]

        last = scores[0].score
        for i in range(1, len(scores)):
            if scores[i].score == last:
                winners.append(scores[i])
            else:
                break

        return winners

    def reset_game(self):
        self.current_player = 0
        self.board.reset()
        for p in self.players:
            p.reset()

