from typing import Dict

import PySimpleGUI as sg


def player_ui_setup(parameters: dict):
    layout = []
    for parameter, (val, descr, cls) in parameters.items():
        layout.append([sg.Text(descr), sg.Input(default_text=val, key=parameter)])

    layout.append([sg.Button(button_text='Done', key='Done')])

    # Create the window
    window = sg.Window("Set Up Player", layout)

    new_parameters = {key: None for key in parameters.keys()}
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Done':
            # loop through and try and convert strings to needed types
            for key in new_parameters.keys():
                val = values[key]
                try:
                    val = parameters[key][2](val)
                except Exception:
                    raise ValueError("Can't convert parameter '%s' with value '%s' to type %s" %
                                     (key, val, parameters[key][2]))

                new_parameters[key] = val
            break

    window.close()
    return new_parameters
