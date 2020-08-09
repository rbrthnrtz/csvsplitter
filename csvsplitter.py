from splitterfunc import split
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Bandwidth File Splitter', font=('Any', 16), justification='center')],
    [sg.Text('_' * 70, pad=(0, 20))],
    [sg.Text('Source File', size=(12, 0)), sg.In(), sg.FileBrowse(size=(10, 1),
                                                                  key='-CSV File-',
                                                                  file_types=(("CSV Files", "*.csv"),),
                                                                  pad=(10, 5))],
    [sg.Text("Output Path", size=(12, 0)), sg.In(),
     sg.FolderBrowse(size=(10, 1), key='-Output-', pad=(10, 5))],
    [sg.Text('_' * 70, pad=(0, 20))],
    [sg.Text("Output Name", size=(12, 1)), sg.In(size=(18, 1), pad=(10, 5),
                                                 key='-Outputname-', default_text='splitter_output',
                                                 tooltip="Default is splitter_output")],
    [sg.Text("Delimiter", size=(12, 1)), sg.In(size=(5, 1), pad=(10, 5),
                                                     key='-Delimiter-', default_text=',',
                                                     tooltip="Input the delimiter type for the .csv file",
                                                     enable_events=True)],
    [sg.Text("Row Limit", size=(12, 1)), sg.In(size=(5, 1), key='-Row Limit-',
                                               tooltip="Default is 5000",
                                               enable_events=True,
                                               pad=(10, 5))],
    [sg.Text('Keep Headers', size=(12, 1)),
     sg.Checkbox('', tooltip="This will keep the header row consistent on split files",
                 key='-Keep Headers-',
                 default=True, pad=(10, 5))],
    [sg.Text('_' * 70, pad=(0, 20))],
    [sg.OK(pad=(10, 20)), sg.Cancel("Exit", pad=(10, 20))]]

window = sg.Window('Bandwidth .csv Splitter', layout, margins=(50, 30))

# main event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
        break
    # this ensures that the delimiter value is only a single valid characters
    if event == '-Delimiter-' and values['-Delimiter-'] and values['-Delimiter-'] not in (',', ':', ';', '.', '|', '^'):
        window['-Delimiter-'].update(values['-Delimiter-'][:0])
    # this ensures that only numbers are entered for the Row Limit
    try:
        if event == '-Row Limit-' and values['-Row Limit-'][-1] not in '0123456789':
            window['-Row Limit-'].update(values['-Row Limit-'][:-1])
    # Cover conditions where box is null which throws an index error
    except:
        pass
    # when Ok is pressed, main split event occurs
    if event == 'OK':
        try:
            if values['-Row Limit-']:
                rowlim = int(values['-Row Limit-'])
            else:
                rowlim = values['-Row Limit-'] = 5000
            # program will attempt to split the file based on the input from the user
            split(filehandler=open(values['-CSV File-']), delimiter=values['-Delimiter-'],
                  row_limit=rowlim,
                  output_name_template='{}_%s.csv'.format(str(values['-Outputname-'])),
                  output_path=values['-Output-'], keep_headers=values['-Keep Headers-'])
            sg.Popup("Success!", auto_close=True, auto_close_duration=5)
        except Exception as e:
            print(e)
            # if there is an error
            sg.Popup("Please enter valid parameters", auto_close=True, auto_close_duration=5)
            continue
