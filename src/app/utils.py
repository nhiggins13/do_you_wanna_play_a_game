from typing import Dict

import PySimpleGUI as sg


def ui_setup(parameters: dict, object_type='') -> dict:
    """
    Creates a popup with the changeable input parameters and their current values. When the done button is clicked
    the user input values are taken, attempted to be converted to the right type and returned in a dictionary


    :param parameters: a dict key: parameter name the values being a tuple (current value, description, type)
    :return: a dictionary key: parameter name, value: value from user
    """

    # create a gui from the given parameters, text for the description and an input box for the value
    layout = []
    for parameter, (val, descr, cls) in parameters.items():
        layout.append([sg.Text(descr), sg.Input(default_text=val, key=parameter)])

    layout.append([sg.Button(button_text='Done', key='Done')])

    # Create the window
    window = sg.Window("Set Up %s" % object_type, layout)

    new_parameters = {key: None for key in parameters.keys()}
    # Create an event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # End program if user closes window
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
