#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:07:51 2023

@author: samkd
"""

l_appointments = [] 

def book_appt():
    """
    An appointment booking system that takes input from user and returns a dictionary
    of appointment slot of choice 
    
    RETURNS
    -------
    appointment slot 
    
    """
    appointment_slot = {"Full Name" :[input("Please enter your full name:" ).upper()] , "date of appointment":[input("Please enter date in yyyy-mm-dd format: ")]}
                        
    return appointment_slot

def see_appointments_taken():
    for item in l_appointments:
        print(list(item.values())[1])