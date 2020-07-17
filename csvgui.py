from csvsplitter import split
import PySimpleGUI as sg
import os.path

sg.theme('Reddit')

layout = [  [sg.Text('Select .csv file to split')],
            [sg.Input(), sg.FileBrowse(key= '-CSV File-', file_types=(("CSV File", "*.csv"),))],


            [sg.Text("Input Delimiter:"), sg.In(size=(8,1),key= '-Delimiter-', default_text= ',')],
            [sg.Text("Row Limit:"), sg.In(size=(8,1), key= '-Row Limit-', default_text=5000)],
            # [sg.Text("Output Name Template"), sg.Input()],
            # [sg.Text("Output Path"), sg.Input()],
            [sg.Checkbox('Keep Headers', key='-Keep Headers-', default=True)],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Bandwidth .csv Splitter', layout)

event, values = window.read()
file = open(values['-CSV File-'])
delimiter1 = values['-Delimiter-']
row_limit1 = int(values['-Row Limit-'])
keep_headers1 = values['-Keep Headers-']

while True:
    if event == 'Cancel':
        break
    try:
        split(file, delimiter=delimiter1, row_limit= row_limit1,
    output_name_template='splitter_output_%s.csv', output_path='.', keep_headers=keep_headers1)
        sg.Popup("Success!")
        window.close()
        break
    except:
        sg.Popup("Error")
        window.close()
        break
