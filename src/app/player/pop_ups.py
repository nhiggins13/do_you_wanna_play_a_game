import os

import PySimpleGUI as sg


def choose_left_right(name) -> str:
    """
    gui for a human player to pick left or right side of the chain

    :param name: name of the player
    :return: 'L' or 'R'
    """

    # layout of the gui, text and two buttons
    layout = [
        [sg.Text(" %s choose what side of the chain to take from:" % name)],
        [sg.Button(button_text='Left', key='Left', size=12), sg.Button(button_text='Right', key='Right', size=12)]
    ]

    # Create the window
    loc = [int(coord) for coord in os.environ['popup_loc'].split(',')] if 'popup_loc' in os.environ else (None, None)
    window = sg.Window("Pick a Side", layout, location=loc)

    result = 'L'  # defaults to left
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Left', 'Right'):  # if left or right button was clicked
            if event == 'Right':
                result = 'R'
            break

    # save the last location of this pop up so it pops up in the same location next time
    os.environ['popup_loc'] = ','.join([str(x) for x in window.current_location()])
    window.close()
    return result
