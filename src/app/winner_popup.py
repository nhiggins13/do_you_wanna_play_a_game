import PySimpleGUI as sg


def winner_popup(winners):
    winner_names = [p.name for p in winners]
    layout = [
        [sg.Text('The winners are %s!' % winner_names)]
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
