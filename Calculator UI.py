#complete calculator with the UI
from unittest import result
import PySimpleGUI as sg                        


Button_size = (4,2)
sg.set_options(font="Franklin 14", element_size=(6,3), element_text_color=(255,255,255))

  


def create_window(theme):
    sg.theme(theme)
    layout = [  [sg.Text("0",font="Franklin 26", justification='left',right_click_menu=theme_menu,key= '-TEXT-', pad=(10,20))],     # Part 2 - The Layout
                [sg.Button(1, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(2, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(3, size=Button_size, mouseover_colors=(128,0,128)), sg.Button("+", size=Button_size, mouseover_colors=(128,0,128))],
                [sg.Button(4, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(5, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(6, size=Button_size, mouseover_colors=(128,0,128)), sg.Button("-", size=Button_size, mouseover_colors=(128,0,128))],
                [sg.Button(7, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(8, size=Button_size, mouseover_colors=(128,0,128)), sg.Button(9, size=Button_size, mouseover_colors=(128,0,128)), sg.Button("*", size=Button_size, mouseover_colors=(128,0,128))],
                [sg.Button(0, size=Button_size, mouseover_colors=(128,0,128)), sg.Button("AC", size=Button_size,expand_x=True, mouseover_colors=(128,0,128)), sg.Button("Enter", size=Button_size,expand_x=True, mouseover_colors=(128,0,128)), sg.Button("/", size=Button_size,expand_x=True, mouseover_colors=(128,0,128))],
                [sg.Button("Themes", size=(6,1), expand_x=True, right_click_menu=theme_menu)]
    ]
              
    return sg.Window('None reliable calculator', layout)



theme_menu = ['menu', ['Lightgrey1', 'DarkBrown4', 'Darkgrey8','DarkTeal',"DarkPurple", 'random']]
window = create_window("DarkBrown4")  
current_num = []
full_operation = []

while True:
    event, values = window.read()   
    if event == sg.WIN_CLOSED:
        break   

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].Update(num_string)
    
    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].Update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation=[]

    if event == "AC":
        current_num = []
        full_operation = []
        window['-TEXT-'].update(" ")
    
window.close() 