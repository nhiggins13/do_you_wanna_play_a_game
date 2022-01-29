from typing import List
import PySimpleGUI as sg
from common.factory import BoardFactory, GameFactory, PlayerFactory
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


def winner_popup(winners: List[Player]):
    """
    Creates a pop up window saying who the winner or winners are.

    :param winners: A list of the winner objects
    :return:
    """
    winner_names = [p.name for p in winners]

    # change the text depending on if there are more than one winner
    if len(winners) > 1:
        text = 'The winners are %s!' % winner_names
    else:
        text = 'The winner is %s' % winner_names[0]

    layout = [
        [sg.Text(text)]
    ]

    # Create the window
    window = sg.Window("Winners", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED:
            break

    window.close()


def chain_game_ui():
    """
    This is the gui for the chain game

    :return:
    """

    # lists to hold the player objects and player names
    players_list = []
    player_names = []

    board = None
    boards = list(BoardFactory.registry.keys())  # list of board types
    games = list(GameFactory.registry.keys())  # list of game types

    # get the player types by game
    players_by_game = {game: [] for game in games}
    for key, p in PlayerFactory.registry.items():
        players_by_game[p.game].append(key)

    # scroll box to hold the player names and scores
    player_scoll = sg.Listbox(values=[], select_mode=sg.SELECT_MODE_EXTENDED, size=(14, 10),
                              key='Player List')

    # scroll box that displays the chain
    board_display = sg.Listbox(values=[], size=(47, 10),  key='board_display')

    # drop down for the game types
    game_drop_down = sg.Combo(games, size=(20, 30), default_value=games[0], key='Game', enable_events=True,
                              readonly=True)

    # drop down for the board types
    board_drop_down = sg.Combo(boards, size=(20, 30), default_value=boards[0], key='Board', enable_events=True,
                               readonly=True)

    # layout of the gui
    layout = [
        [sg.Text('Game:', size=19), sg.Text('Board:', size=20)],
        [game_drop_down, board_drop_down],
        [sg.Text('Players and Scores:', size=14), sg.Text('Current Board:', size=19)],
        [player_scoll, board_display],
        [sg.Button('Add Player', key="add_player", size=(12, 2)),
         sg.Button('Remove Player', key="remove_player", size=(12, 2)),
         sg.Button('Play!', key="play", size=(12, 2)),
         sg.Button('Replay!', key="replay", size=(12, 2), disabled=True)],
    ]

    # Create the window
    window = sg.Window("Chain Game", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED:
            break
        elif event == 'add_player':
            # if the add button is clicked, create a add player popup and update the players list
            new_players = add_player_popup(values['Game'], players_by_game)
            players_list += new_players
            player_names += [p.name for p in new_players]
            window['Player List'].update([name + ': 0' for name in player_names])
        elif event == 'remove_player':
            # if the remove button is clicked, remove the selected players and update the players list
            p_name = values['Player List']
            for p in p_name:
                colon_idx = p.index(':')
                idx = player_names.index(p[:colon_idx])
                player_names.pop(idx)
                players_list.pop(idx)
            window['Player List'].update([name + ': 0' for name in player_names])
        elif event == 'play' or event == 'replay':
            # if the play or replay button is hit start a game

            # if play, create a new board and set parameters with popup,
            # then create a new game and set parameters with a pop up
            if event == 'play':
                board = BoardFactory.create(values['Board'])
                board.gui_setup()
                game = GameFactory.create(values['Game'], players=players_list, board=board)
                game.gui_setup()
            else:  # if replay was hit reset the game, this will be the same exact board and game as just played
                game.reset_game()

            # break up the chain and display
            str_board = [str(x) for x in board.values]
            window['board_display'].update([', '.join(str_board[i:i+10]) for i in range(0, len(str_board), 10)])
            window.refresh()

            while game.end_condition():  # check for the end of the game
                game.play_turn()  # play a single turn

                # break up the board and update display
                str_board = [str(x) for x in board.values]
                window['board_display'].update([', '.join(str_board[i:i + 10]) for i in range(0, len(str_board), 10)])

                # get scores and update players scroll box
                scores = game.get_scores()
                window['Player List'].update([name + ': ' + str(score) for name, score in zip(player_names, scores)])

                window.refresh()

            # get the winners and create a popup
            winners = game.get_winner()
            winner_popup(winners)
            window['replay'].update(disabled=False) # enable the replay button

    window.close()


if __name__ == '__main__':
    chain_game_ui()

