#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:07:51 2023

@author: samkd
"""
from datetime import datetime

def book_appt():
    """
    An appointment booking system that takes input from user and returns a dictionary
    of appointment slot of choice 
    Will use datetime conditions for dates
    RETURNS
    -------
    appointment slot 
    
    """
    try:
        f_name = input("Please enter your first name:").upper()
        l_name = input("Please enter your last name: ").upper()
        date = input("Please enter date of your choice in yyyy-mm-dd format: ")
        appointment_slot = [{"First name": f_name}, {"Last name": l_name}, {"Date of appointment": date}]
        appointment_slot[2]["Date of appointment"] = datetime.strptime(appointment_slot[2]["Date of appointment"], "%Y-%m-%d")
        if appointment_slot["date of appointment"] < datetime.today():
            print(""""Date has to be after today. Try again.""")
        else:
            print(appointment_slot)
            return appointment_slot
        
    except:
        print(""""Sorry you may have entered the date incorrectly.
              \n Please try again, remember to use YYYY-MM-DD format""")
              
    


book_appt()
    