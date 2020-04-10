import logging
import time
from tkinter import *

import numpy as np
from rtmidi.midiutil import open_midiinput

import midi_constants.py

# ROOT WINDOW
root = Tk()
root.title("Piano")
width = 1300
height = 624
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Create Canvas to hold the barchart, text, etc.
c = Canvas(root, width=width, height=height, bd=0, highlightthickness=0, bg="red")
c.grid(rowspan=30, row=0, column=0)
txt = Label(root, text="Dynamics")
txt.configure(font="Georgia 20 bold", foreground="#efcf83", bg="#161616")
txt.grid(row=0, column=0)
# piano_photo = PhotoImage(file='piano_3.png')
c.piano_image = PhotoImage(file='piano_3.png')
c.piano_image_id = c.create_image(1300, 624, image=c.piano_image)
c.move(c.piano_image_id, -650, -312)

# Configure the shape and size of chart to properly fit the window and image background
y_gap = 182                 # The gap between lower canvas edge and x axis
y_stretch = 3               # The highest y = max_data_value * y_stretch
y1_const = height - y_gap   # y position on bottom of bars (x-axis), constant, does not change
y0_init = y1_const - 3      # height of bars when not active, initial default position
x_gap = 80                  # The gap between left canvas edge and y axis
x_stretch = 1.25            # Stretch x wide enough to fit the variables
x_width = 11.5              # The width of the x-axis

# Initialize rtmidi and open port
log = logging.getLogger('midiin_poll')  # '''INITIALIZE MIDI CAPTURE'''
port = sys.argv['1'] if len(
    sys.argv) > 1 else '0'  # Prompts for MIDI port, unless a valid port is given in first argument on command line.
try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()
print("Entering main loop. Press Control-C to exit.")


def closest(lst, k):  # Used for calculating closest dynamics variable from velocity integer
    lst = np.asarray(lst)
    idx = (np.abs(lst - k)).argmin()
    return lst[idx]


# CLOSE HANDLER
def close(event):
    root.withdraw()  # if you want to bring it back
    sys.exit()  # if you want to exit the entire thing
    print("Exit.")
    midiin.close_port()
    del midiin


# bind escape key to the above close function
root.bind('<Escape>', close)

# tkinter After loop
def task():
    timer = time.time()
    msg = midiin.get_message()
    if msg:
        message, deltatime = msg
        midi_key = int(message[1])
        piano_key = midikeyDict[midi_key]

        if int(message[0]) == 144:
            timer += deltatime
            midi_velocity = int(message[2])
            rounded_velocity = closest(dynamics_lst, midi_velocity)
            dynamics = dynamicsDict[rounded_velocity]
            txt.configure(text=str(dynamics))
            txt.update()  # update text at top of GUI with dynamics variable
            x0 = piano_key * x_stretch + piano_key * x_width + x_gap  # visible LEFT
            y0 = 624 - y_gap - midi_velocity * y_stretch  # visible TOP - newly calculated
            x1 = piano_key * x_stretch + piano_key * x_width + x_gap + x_width  # visible RIGHT
            c.create_rectangle(x0, y0_init, x1, y1_const, fill='grey') # create initial bar that we will update
            find_rect_id = c.find_closest(x1, y1_const)[0]  # get tkinter id of the rectangle at piano_key coordinates
            curr_height = c.coords(find_rect_id)[1]  # y0 (y top) at base level that we will increase
            while curr_height > y0:
                curr_height -= 0.2
                c.coords(find_rect_id, x0, curr_height, x1, y1_const)
            # TODO put this into the constants file
            if dynamics == 'pp':
                c.itemconfig(find_rect_id, fill='#71C7E7')
            elif dynamics == 'p':
                c.itemconfig(find_rect_id, fill='#009FDA')
            elif dynamics == 'mf':
                c.itemconfig(find_rect_id, fill='#A54499')
            elif dynamics == 'f':
                c.itemconfig(find_rect_id, fill='#FD663F')
            elif dynamics == 'ff':
                c.itemconfig(find_rect_id, fill='#FD2D26')
                
        elif int(message[0]) == 128:
            timer += deltatime
            x0 = piano_key * x_stretch + piano_key * x_width + x_gap            # visible LEFT
            x1 = piano_key * x_stretch + piano_key * x_width + x_width + x_gap  # visible RIGHT
            # y0 and y1 are referenced in initial variables: y0_init and y1_const
            find_rect_id = c.find_closest(x1, y1_const)[0]  # get tkinter id of the rectangle at piano_key coordinates
            curr_height_d = c.coords(find_rect_id)[1]  # current visible TOP to calculate slide out transition
            while curr_height_d < y0_init:  # attempt to slide the bar into position
                curr_height_d += 0.02
                c.coords(find_rect_id, x0, curr_height_d, x1, y1_const)  # reset bar height on note-off
            c.delete(find_rect_id)
        root.after(1, task)
    else:
        root.after(1, task)

# RUN APP
root.after(1, task)
root.mainloop()