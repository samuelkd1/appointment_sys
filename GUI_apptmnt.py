#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""
from tkinter import *

root = Tk()
# title of program
root.title("The appointment booking system Admin")
root.geometry("800x800")
#root.eval('tk::PlaceWindow . center')
Label_1 = Label(root, text = "Welcome to the appointment booking system\n Please choose your options", font = ("Futuristic", 25))
Label_1.pack()

# create some modes

MODES = ["Book appointment", "See booked appointments", "Edit appointments"]
selection = StringVar()
selection.set("Book appointment")
for text, mode in enumerate(MODES):
	Radiobutton(root, text = mode, variable = selection, value = mode).pack()

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

# will make radio buttons

Button_click = Button(root, text = "Select choice", command = lambda: clicked(selection.get()))
Button_click.pack() 

root.mainloop()