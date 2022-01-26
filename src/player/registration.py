from common.utils import register
from common.factory import PlayerFactory
from player.interface import Player


class HumanPlayer(Player):
    is_bot = False


@register('HumanChain', PlayerFactory)
class HumanChainPlayer(HumanPlayer):
    game = 'Chain'

    def play_turn(self, *args, **kwargs):
        #generate a pop up with the options left or right
        pass
