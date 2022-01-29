from numpy.random import RandomState

from app.player.pop_ups import choose_left_right
from common.utils import register
from common.factory import PlayerFactory
from player.interface import Player


class HumanPlayer(Player):
    """
    base class for human players
    """
    is_bot = False


class ChainPlayer(Player):
    """
    base class for chain game players
    """
    game = 'ChainGame'


@register('HumanChain', PlayerFactory)
class HumanChainPlayer(HumanPlayer, ChainPlayer):
    """
    Implementation of a human chain game player
    """
    def play_turn(self, *args, **kwargs) -> str:
        """
        player makes their turn by choosing left or right
        :param args:
        :param kwargs:
        :return: 'L' or 'R'
        """
        side = choose_left_right(self.name)  # pop up gui to decide left or right
        return side


@register('OneSidedChainBot', PlayerFactory)
class OneSidedChainBot(ChainPlayer):
    """
    A bot player that only picks from one side
    """

    def __init__(self, side='L', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = side  # set the side the bot chooses

    def play_turn(self, *args, **kwargs) -> str:
        """
        player makes their turn, will only return their chosen side
        :param args:
        :param kwargs:
        :return: 'L' or 'R'
        """
        return self.side

    def get_params(self):
        """
        This method returns the initialization parameters of the board
        :return: a dictionary of the initialization parameters of the board
        """
        params = super().get_params()
        params['side'] = ('L', 'Side the bot chooses L or R', str)

        return params


@register('GreedyChainBot', PlayerFactory)
class GreedyChainBot(ChainPlayer):
    """
    This bot looks at the two links on the left and the two links on the right
    the inner links are subtracted from the outer links and the larger sum is chosen

    """

    def play_turn(self, board, *args, **kwargs) -> str:
        """
        player makes their turn

        This bot looks at the two links on the left and the two links on the right
        the inner links are subtracted from the outer links and the larger sum is chosen
        :param board:
        :param args:
        :param kwargs:
        :return: 'L' or 'R'
        """

        if len(board.values) != 1:
            left = board.values[0] - board.values[1]  # minus inner from outer left side
            right = board.values[-1] - board.values[-2]  # minus inner from outer right side

            if right > left:
                return 'R'

        return 'L'


@register('RandomChainBot', PlayerFactory)
class RandomChainBot(ChainPlayer):
    """
    This bot randomly chooses a side
    """

    def __init__(self, seed=123, **kwargs):
        super().__init__(**kwargs)
        self.seed = seed  # set the seed
        self.random_state = RandomState(seed)  # set the random state

    def play_turn(self, *args, **kwargs):
        """
        The player makes their turn

        randomly chooses a side
        :param args:
        :param kwargs:
        :return:
        """
        if self.random_state.randint(0, 10) < 5:
            return 'L'
        else:
            return 'R'

    def reset(self):
        """
        reset the player
        :return:
        """
        super().reset()
        self.random_state = RandomState(self.seed)

    def get_params(self):
        """
        This method returns the initialization parameters of the board
        :return: a dictionary of the initialization parameters of the board
        """
        params = super().get_params()
        params['seed'] = (self.seed, 'Random seed', int)

        return params
