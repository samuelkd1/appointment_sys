#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 00:26:30 2023

@author: samkd

"""
import pandas as pd
from datetime import datetime

def book_appt():
    """
    An appointment booking system that takes input from user and returns a dictionary
    of appointment slot of choice 
    
    Returns
    -------
    appointment slot 
    
    """
    try:
        appointment_slot = {"Full Name" :[input("Please enter your full name:" ).upper()] , "date of appointment":[input("Please enter date in yyyy-mm-dd format: ")]}
        appointment_slot["date of appointment"] = datetime.strptime(appointment_slot["date of appointment"][0], "%Y-%m-%d") 
        appointment_slot["Full Name"] = appointment_slot["Full Name"][0]
        if appointment_slot["date of appointment"] < datetime.today():
            print(""""Date has to be after today. Try again.""")
        
        else:
            return appointment_slot
    
    except:
        print(""""Sorry you may have entered the date incorrectly.
              \n Please try again, remember to use YYYY-MM-DD format""")

def see_appointments_taken():
    """
    See the appointments that have already been taken 

    Returns
    -------
    None. Prints slots instead

    """
    for item in l_appointments:
        print(item["date of appointment"])

def menu():
    """
    A menu that does certain commands depending on the number chosen. 
    For almost all of the actions the data needs to be read and all test data 
    needs to be retrieved.

    Returns
    -------
    None.
    """
    global l_appointments
    l_appointments = [] 
    ans = True
    while ans:
        print("""1. BOOK APPOINTMENT
              \n2. VIEW TAKEN SLOTS
              \n3. EXIT"""
              )
        ans = input("PLEASE SELECT AN OPTION : ") 
        if ans == "1":
            appointment_slot = book_appt()
            if appointment_slot not in l_appointments:
                    l_appointments.append(appointment_slot)
            else:
                print("sorry slot taken, try again")
        
        if ans == "2":
            if len(l_appointments) >= 1:
                see_appointments_taken()
                print("Above are the unavailable dates")
            
            else:
                print("""All slots are free for now, you can now book.
                      \nIf this changes we will alert you""")           
            
        if ans == "3":
            
            if len(l_appointments) < 1:
                print("""\nThank you for using this system.
                      \ngoodbye""")
                break
            
            else:
                print("""\nThank you for using this system. 
                      \nYour appointments have now been added to the system 
                      """)
                global df
                df = pd.DataFrame(l_appointments)
                df.to_csv("booked_appointments.csv", mode = "a" )
                break





   

