from splitterfunc import split
import PySimpleGUI as sg
import os.path

sg.theme('LightBlue7')

layout = [  [sg.Text('.csv File Splitter', font=('Helvetica', 16))],
            [sg.Text('Source File:'), sg.In(), sg.FileBrowse(size=(8,1), key= '-CSV File-', file_types=(("CSV File", "*.csv"),))],
            [sg.Text("Input Delimiter:"), sg.In(size=(8,1),key= '-Delimiter-', default_text= ',', enable_events= True)],
            [sg.Text('Default is comma')],
            [sg.Text("Row Limit:"), sg.In(size=(8,1), key= '-Row Limit-', default_text=5000, enable_events= True)],
            [sg.Text('Defualt is 5000')],
            [sg.Text("Output Name:"), sg.In(size=(18,1), key= '-Outputname-', default_text='splitter_output',)],
            [sg.Text('Defualt is _N file directory')],
            [sg.Text("Output Path:"), sg.In(), sg.FolderBrowse(size=(8,1), key= '-Output-')],
            [sg.Text('Default is working directory')],
            [sg.Checkbox('Keep Headers', key='-Keep Headers-', default=True)],
            [sg.OK(), sg.Cancel()]  ]

window = sg.Window('Bandwidth .csv Splitter', layout)

#event loop
while True:
    event, values = window.read()
    print(event)
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    #this ensures that the delimiter value is only a single valid characters
    if event == '-Delimiter-' and values['-Delimiter-'] and values['-Delimiter-'] not in (':',';',',','.','|'):
        window['-Delimiter-'].update(values['-Delimiter-'][:0])
    #this ensures that only numbers are entered for the Row Limit
    if event == '-Row Limit-' and values['-Row Limit-'] and values['-Row Limit-'][-1] not in ('0123456789'):
        window['-Row Limit-'].update(values['-Row Limit-'][:-1])
    #when Ok is pressed, main split event occurs
    if event == 'OK':
        try:
            if values['-Row Limit-']:
                rowlim= int(values['-Row Limit-'])
            else:
                rowlim = values['-Row Limit-'] = 50
            #program will attempt to split the file based on the input from the user
            split(filehandler= open(values['-CSV File-']) , delimiter=values['-Delimiter-'],
                    row_limit= rowlim,
                    output_name_template='{}_%s.csv'.format(str(values['-Outputname-'])),
                    output_path=values['-Output-'], keep_headers=values['-Keep Headers-'])
            sg.Popup("Success!")
        except Exception as e:
            print(e)
            #if there is an error
            sg.Popup("Please enter valid parameters")
            continue
