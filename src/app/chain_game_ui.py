import PySimpleGUI as sg

from app.add_player_ui import add_player_popup
from app.winner_popup import winner_popup
from common.factory import BoardFactory, GameFactory, PlayerFactory


def chain_game_ui():
    players_list = []
    player_names = []

    board = None

    boards = list(BoardFactory.registry.keys())
    games = list(GameFactory.registry.keys())

    players_by_game = {game: [] for game in games}
    for key, p in PlayerFactory.registry.items():
        players_by_game[p.game].append(key)

    player_scoll = sg.Listbox(values=player_names, select_mode=sg.SELECT_MODE_EXTENDED, size=(10, 10),
                              key='Player List')

    board_display = sg.Listbox(values=[], size=(47, 10),  key='board_display')

    game_drop_down = sg.Combo(games, size=(20, 30), default_value=games[0], key='Game', enable_events=True,
                              readonly=True)

    board_drop_down = sg.Combo(boards, size=(20, 30), default_value=boards[0], key='Board', enable_events=True,
                               readonly=True)

    layout = [
        [sg.Text('Game:', size=19), sg.Text('Board:', size=20)],
        [game_drop_down, board_drop_down],
        [sg.Text('Players:', size=11), sg.Text('Current Board:', size=19)],
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
            new_players = add_player_popup(values['Game'], players_by_game)
            players_list += new_players
            player_names += [p.name for p in new_players]
            window['Player List'].update(player_names)
        elif event == 'remove_player':
            p_name = values['Player List']
            for p in p_name:
                idx = player_names.index(p)
                player_names.pop(idx)
                players_list.pop(idx)
            window['Player List'].update(player_names)
        elif event == 'play' or event == 'replay':

            if event == 'play':
                board = BoardFactory.create(values['Board'])
                board.gui_setup()
                game = GameFactory.create(values['Game'], players=players_list, board=board)
                game.gui_setup()
            else:
                game.reset_game()

            window['board_display'].update([', '.join([str(x) for x in board.values])])
            window.refresh()

            while game.end_condition():
                game.play_turn()
                window['board_display'].update([', '.join([str(x) for x in board.values])])
                window.refresh()
            winners = game.get_winner()
            winner_popup(winners)
            window['replay'].update(disabled=False)
            print('winners: %s' % winners)

    window.close()


if __name__ == '__main__':
    chain_game_ui()

