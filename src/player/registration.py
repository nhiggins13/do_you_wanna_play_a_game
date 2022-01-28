from abc import ABC
from numpy.random import RandomState
from common.utils import register
from common.factory import PlayerFactory
from player.interface import Player


class HumanPlayer(Player):
    is_bot = False


class ChainPlayer(Player):
    game = 'Chain'


@register('HumanChain', PlayerFactory)
class HumanChainPlayer(HumanPlayer, ChainPlayer):
    def play_turn(self, *args, **kwargs):
        print(kwargs['board'].values)
        side = input('%s pick a side left(L) or right(R):' % self.name)
        return side


@register('OneSidedChainBot', PlayerFactory)
class OneSidedChainBot(ChainPlayer):

    def __init__(self, side='L', **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def play_turn(self, *args, **kwargs):
        return self.side


@register('GreedyChainBot', PlayerFactory)
class GreedyChainBot(ChainPlayer):

    def play_turn(self, board, *args, **kwargs):
        if len(board.values) != 1:
            left = board.values[0] - board.values[1]
            right = board.values[-1] - board.values[-2]

            if right > left:
                return 'R'

        return 'L'


@register('RandomChainBot', PlayerFactory)
class RandomChainBot(ChainPlayer):

    def __init__(self, seed, **kwargs):
        super().__init__(**kwargs)
        self.random_state = RandomState(seed)

    def play_turn(self, *args, **kwargs):
        if self.random_state.randint(0,10) < 5:
            return 'L'
        else:
            return 'R'
