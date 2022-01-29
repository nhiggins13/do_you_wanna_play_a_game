from abc import ABC
from numpy.random import RandomState
from common.utils import register
from common.factory import PlayerFactory
from player.interface import Player


class HumanPlayer(Player):
    is_bot = False


class ChainPlayer(Player):
    game = 'ChainGame'


@register('HumanChain', PlayerFactory)
class HumanChainPlayer(HumanPlayer, ChainPlayer):
    def play_turn(self, *args, **kwargs):
        print(kwargs['board'].values)
        side = input('%s pick a side left(L) or right(R):' % self.name)
        return side


@register('OneSidedChainBot', PlayerFactory)
class OneSidedChainBot(ChainPlayer):

    def __init__(self, side='L', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = side

    def play_turn(self, *args, **kwargs):
        return self.side

    def get_params(self):
        params = super().get_params()
        params['side'] = ('L', 'Side the bot chooses L or R', str)

        return params


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

    def __init__(self, seed=123, **kwargs):
        super().__init__(**kwargs)
        self.seed = seed
        self.random_state = RandomState(seed)

    def play_turn(self, *args, **kwargs):
        if self.random_state.randint(0,10) < 5:
            return 'L'
        else:
            return 'R'

    def reset(self):
        super().reset()
        self.random_state = RandomState(self.seed)

    def get_params(self):
        params = super().get_params()
        params['seed'] = (self.seed, 'Random seed', int)

        return params
