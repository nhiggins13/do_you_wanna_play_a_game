from common.factory import PlayerFactory
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from game.registration import ChainGame
from player.registration import HumanChainPlayer, GreedyChainBot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players = [HumanChainPlayer(name='Nick'), GreedyChainBot(name='Greedy')]
    winner = ChainGame(players=players).play()
    print('Winners: %s' % [p.name for p in winner])

