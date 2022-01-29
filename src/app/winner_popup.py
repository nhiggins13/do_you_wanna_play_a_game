import PySimpleGUI as sg


def winner_popup(winners):
    winner_names = [p.name for p in winners]
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
