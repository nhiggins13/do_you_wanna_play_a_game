import PySimpleGUI as sg

def focus_control(event):
    if window['myInput'].get() == '':
        window['myInput'].update(value=default_text)
    window['myInput'].update(select=True)
    # window.refresh()
    return None

default_text = "deleteMeOnClick"
layout = [[sg.InputText(default_text, size=(50, 1), key='myInput')],
          [sg.InputText(default_text, size=(50, 1), enable_events=True, key='myInput2')],
          [sg.Button("OK")],
          [sg.Text('', size=(50, 1), key='Message')]]
window = sg.Window("A title", layout, finalize=True)
window['myInput'].Widget.bind("<FocusIn>", focus_control)
window['myInput'].update(select=True)

while True:

    event, values = window.read()
    print(event, values)
    if event == None:
        break
    elif event == 'OK':
        window['Message'].update(value=values['myInput'])

window.close()