from typing import List

import PySimpleGUI as sg
from common.factory import PlayerFactory
from player.interface import Player


def add_player_popup(game, players_by_game) -> List[Player]:
    """
    Creates a pop up with a drop down menu of player types for the game. The user selects a player type, types a name
    and hits the add button. When done adding players hit the add button.

    :param game: The name of the game to be played
    :param players_by_game: a dictionary of players types by game
    :return: a list of players to be added to the game
    """
    player_types = players_by_game[game] # get the player types for this game

    # layout of the pop up gui
    add_player_layout = [
        [sg.Combo(player_types, size=(20, 20), default_value=player_types[0], key='player_type', enable_events=True,
                  readonly=True)],
        [
            [sg.Input(default_text='Enter player name', do_not_clear=False, key='player_name', size=(22, 20))],
            [sg.Button(button_text='Add', key='button_add_player'), sg.Button(button_text='Done', key='Done')]
        ]
    ]

    # Create the window
    window = sg.Window("Add Players", add_player_layout)

    players = []
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED or event == 'Done':
            break
        elif event == 'button_add_player':


            # create the player and add it to the list of players to be added
            player = PlayerFactory.create(values['player_type'], name=values['player_name'])
            player.gui_setup()
            players.append(player)

    window.close()
    return players