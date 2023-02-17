#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""
from tkinter import *

root = Tk()
root.title("The appointment booking system")
root.geometry("800x800")
#root.eval('tk::PlaceWindow . center')
Label_1 = Label(root, text = "Welcome to the appointment booking admin system\n Please choose your options", font = ("Futuristic", 25))
Label_1.pack()

root.mainloop()