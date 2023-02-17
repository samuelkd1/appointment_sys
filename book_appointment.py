#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:07:51 2023

@author: samkd
"""

def book_appt():
    """
    An appointment booking system that takes input from user and returns a dictionary
    of appointment slot of choice 
    Will use datetime conditions for dates
    RETURNS
    -------
    appointment slot 
    
    """
    f_name = input("Please enter your first name:").upper()
    l_name = input("Please enter your last name: ").upper()
    date = input("Please enter date in yyyy-mm-dd format: ")
    appointment_slot = [{"First name": f_name}, {"Last name": l_name}, {"Date of appointment": date}]
                        
    return appointment_slot


book_appt()
    