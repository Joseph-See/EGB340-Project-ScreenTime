# GUI to display images

import PySimpleGUI as sg
import os.path

layout = [[sg.Text("Time to take a break!", size = (750, 750), justification='center')]] 
#[sg.Image("standingUp.gif", "stand")]]

window = sg.Window("BreakTime", layout=layout, size = (500, 500))

while True:
    # Use timeout so GUI is responsive to both user input and animating the gif
    event, values = window.Read(timeout=42) 
    #sg.popup_animated("standingUp.gif", background_color='white', time_between_frames=42, transparent_color='white')
    sg.Image("standingUp.gif", visible =  True).update_animation_no_buffering
    if event == sg.WIN_CLOSED:
        break
    elif event is None:
        break

window.close()