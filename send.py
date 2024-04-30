import serial
import time

import PySimpleGUI as sg

arduino = serial.Serial(port='COM10',  baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    # time.sleep(0.05)
    # data = arduino.readline()
    # return  data

layout = [[sg.Text("Turn led on")], [sg.Button("ON"), sg.Button("OFF")],]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "ON":
        write_read("23")
    elif event == "OFF":
        write_read("13")
    if event == sg.WIN_CLOSED:
        break

window.close()
