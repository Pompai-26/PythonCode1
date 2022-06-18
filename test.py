import PySimpleGUI as sg
from .PySimpleGUI import *
import tkinter as tk
import _tkinter

layout = [[sg.Text("Welcome to Moumita's World")], [sg.Text('Please enter your Name')],
    [sg.Text('Name', size =(15, 1)), sg.InputText()], [sg.Text("", size=(15, 1), key='OUTPUT')], [sg.Button("OK")], [sg.Button("QUIT")], [sg.Image('D:\Alu\Test.png')]]
# Create the window
window = sg.Window("Demo", layout, margins=(100, 100))


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "QUIT" or event == sg.WIN_CLOSED:
        break
    if event == "OK":
        name = values[0]
        window['OUTPUT'].update(value=name)

        sg.popup('Hello', name, 'Welcome to My World')




window.close()
