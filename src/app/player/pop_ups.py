import os

import PySimpleGUI as sg


def choose_left_right(name):
    layout = [
        [sg.Text(" %s choose what side of the chain to take from:" % name)],
        [sg.Button(button_text='Left', key='Left', size=12), sg.Button(button_text='Right', key='Right', size=12)]
    ]

    # Create the window
    loc = [int(coord) for coord in os.environ['popup_loc'].split(',')] if 'popup_loc' in os.environ else (None, None)
    window = sg.Window("Pick a Side", layout, location=loc)

    result = 'L'
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Left', 'Right'):
            if event == 'Right':
                result = 'R'
            break

    os.environ['popup_loc'] = ','.join([str(x) for x in window.current_location()])
    window.close()
    return result
