import PySimpleGUI as sg


def choose_left_right(name):
    layout = [
        [sg.Text(" %s choose what side of the chain to take from:" % name)],
        [sg.Button(button_text='Left', key='Left', size=12), sg.Button(button_text='Right', key='Right', size=12)]
    ]

    # Create the window
    window = sg.Window("Pick a Side", layout)

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

    window.close()
    return result
