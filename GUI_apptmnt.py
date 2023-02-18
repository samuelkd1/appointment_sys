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

# will make radio buttons

Radiobutton(root, text = "Book appointment").pack()
Radiobutton(root, text = "See booked appointments").pack()
Radiobutton(root, text = "Edit appointments").pack()

Button_click = Button(root, text = "select")
Button_click.pack() 

root.mainloop()