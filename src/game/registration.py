from typing import List

from board.interface import Board
from common.utils import register
from common.factory import GameFactory
from game.interface import Game
from player.interface import Player


@register('ChainGame', GameFactory)
class ChainGame(Game):
    """
    Implementation of the Chain game
    """
    player_names = set()
    board = None

    def __init__(self, players: List[Player], board: Board):
        """
        sets the starting player
        checks the players are unique
        sets the board
        :param players: list of player objects
        :param board: instance of a board
        """
        self.current_player = 0
        if self._check_unique_player_names(players):
            self.players = players
            self.player_names = set(p.name for p in players)
        else:
            raise ValueError('Player names not unique')

        self.board = board

    def _check_unique_player_names(self, players: List[Player]) -> bool:
        """
        check players are unique
        :param players: list of player objects
        :return: True if the players are unique
        """
        if isinstance(players, list):
            if len(players) == len(set(p.name for p in players)):
                return True
            return False
        elif players.name in self.player_names:
            return False

        return True

    def add_player(self, player):
        """
        add player to the game
        :param player: player object
        :return:
        """

        # check if the player name already exists
        if player.name in self.player_names:
            raise ValueError('Player name %s already in the game' % player.name)

        # adds the player to player and name lists
        self.players.append(player)
        self.player_names.add(player.name)

    def remove_player(self, player_name: str):
        """
        finds and removes a player
        :param player_name: name of a player in the game
        :return:
        """

        # find and remove player
        if player_name in self.player_names:
            for i, p in enumerate(self.players):
                if p.name == player_name:
                    self.players.pop(i)
                    break

            self.player_names.remove(player_name)

    def end_condition(self):
        """
        checks if the board has items left
        :return:
        """
        return True if self.board.values else False

    def play_turn(self):
        """
        Play a turn of the game
        :return:
        """
        turn = self.players[self.current_player].play_turn(board=self.board)  # have player make a decision
        val = self.board.interact(side=turn)  # pop value from the board
        self.players[self.current_player].score += val  # update the player's score
        self.update_turn()  # update who's turn it is

    def update_turn(self):
        """
        update who's turn it is
        :return:
        """
        self.current_player += 1  # increment the index of the current player
        if self.current_player >= len(self.players):  # reset to 0 if the index is greater than the player list
            self.current_player = 0

    def get_winner(self) -> List[Player]:
        """
        return a list of winners
        :return: a list of the winning player objects
        """
        scores = sorted(self.players, key=lambda p: -p.score)
        winners = [scores[0]]

        # loop until the score is not equal to the last
        last = scores[0].score
        for i in range(1, len(scores)):
            if scores[i].score == last:
                winners.append(scores[i])
            else:
                break

        return winners

    def reset_game(self):
        """
        reset the game
        :return:
        """
        self.current_player = 0  # set the current player
        self.board.reset()  # reset the board
        for p in self.players:  # reset the players
            p.reset()

