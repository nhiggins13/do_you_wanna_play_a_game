from src.common.utils import make_factory_class

# create factories
BoardFactory = make_factory_class('BoardFactory')
PlayerFactory = make_factory_class('PlayerFactory')
GameFactory = make_factory_class('GameFactory')

# import the registration modules so the classes are registered
import player.registration
import board.registration
import game.registration