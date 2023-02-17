#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:45:57 2023

@author: samkd
"""

from tkinter import *

window = Tk()

L1 = Label(window, text="Full Name")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)

window.mainloop()