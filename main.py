import numpy as np
import pandas as pd
import PySimpleGUI as sg


df = pd.read_csv('Ship Resource Logistics.csv')
#print(df)
Array2d_result = df.to_numpy()
#print(Array2d_result)
#print(Array2d_result[:,0])    


sg.theme("Darkteal9")

layout = [
    #light time cost
    [sg.Text('Light Ship Time Cost Reduction:')],
    [sg.Text('Fleet Docks'),
    sg.Combo([1,2,3,4,5,6,7,8,9,10]),
    sg.Text('Docking Bay'),
    sg.Combo([1,2,3,4,5,6,7,8,9,10])],
    [sg.Checkbox('Royal Pilot School', default=True),
    sg.Checkbox('Station Rune', default=True),  
    sg.Checkbox('Gatos Org', default=True)],
    [sg.Text('Patrol Policy'),
    sg.Combo([1,2,3,4,5]),
    sg.Text('Viva La Resistance'),
    sg.Combo([1,2,3,4,5]),
    sg.Text('Scout Policy'),
    sg.Combo([1,2,3,4,5])],
    
    #light rss cost
    [sg.Text('Light Ship Rss Cost')],
    [sg.Text('Policy: Frontier Piracy'),
    sg.Combo([1,2,3,4,5]),
    sg.Text('Policy: Cartography'),
    sg.Combo([1,2,3,4,5]),
    sg.Text("Policy: Trucker's Union"),
    sg.Combo([1,2,3,4,5]),
    sg.Text("Huang's Regional"),
    sg.Combo([1,2,3,4,5])],
    
    #heavies and capitals time cost
    [sg.Text('Heavy & Capital Ship Time Cost Reduction:')],
    [sg.Text('Moon Points'),
    sg.Combo([1,2,3,4,5,6,7,8,9,10]),
    sg.Text('MIC'),
    sg.Combo([1,2,3,4,5,6,7,8,9,10]),
    sg.Text('HSA'),
    sg.Combo([1,2,3,4,5])],
    
    
    #heavies and capitals cost
    [sg.Text('Heavy & Capital Rss Cost')],
    [sg.Checkbox('Orbital Symphonica', default=True)],
    [sg.Checkbox('Station Rune', default=True)],
    [sg.Text("Huang's Regional"),
    sg.Combo([1,2,3,4,5]),
    sg.Text('Dess Policy'),
    sg.Combo([1,2,3,4,5])],
    
    [sg.Submit(),sg.Exit()]
]



window = sg.Window('Salamander', layout, margins=(100,50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
window.close()