#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:07:23 2023

@author: samkd
"""

# This will be something that does three things.
# 1) input full name and date into dictionary and it cannot be repeated 
# 2) this will be written on an excel file 
# 3) dates cannot be repeated 
# 4) notifications will be sent on day of the appointment (hopefully)
# 5) will be put on html for clients to access and book 




#booking system 
#def enter_booking():
"""
This will be the part where we get users to enter the booking dates 
they want.
    
"""


def book_appt():
    appointment_slots = {"Full Name" : input("Please enter your full name:" ).upper() , "date of appointment":input("Please enter date in yyyy-mm-dd format: ")}
    if appointment_slots not in l_appointments:
            l_appointments.append(appointment_slots)
            print(l_appointments)
    else:
        print("sorry slot taken, try again")
       
    
    return l_appointments

print(l_appointments)

def see_appointments_taken():
    for item in l_appointments:
        print(item)


    
#for i in l_appointments:
    #print(i)

"""
while x<2:
    appointment_slots["Full Name"] = 
    appointment_slots["date of appointment"] = date_of_appointment = 
    
    if appointment_slots.values() not in list_of_appointments:
        list_of_appointments.append(appointment_slots)
    else: 
        print("your appointment is taken please choose another appointment slot try again")
    x+= 1
    print(list_of_appointments)

"""
    
"""
list_of_appointments = []
appointment_slots = {"Full Name" :[] , "date of appointment":[] }    
x = 0
while x<2:
    appointment_slots["Full Name"] = input("Please enter your full name:" ).upper()
    appointment_slots["date of appointment"] = date_of_appointment = input("Please enter date in yyyy-mm-dd format: ")
    if appointment_slots.values() not in list_of_appointments:
        list_of_appointments.append(appointment_slots)
    else: 
        print("your appointment is taken please choose another appointment slot try again")
    x+= 1
    print(list_of_appointments)
           
   """         


   
    
#return all_appoints
    

#enter_booking()


# every time I input appointment slot I want it to go into the set 

"""
def put_on_file(appointment_slot):
 
    list_of_appointments = []
    
    while True:
        set(list_of_appointments.append(appointment_slots))
    
    print("Your appointment has been booked successfully")
    print(appointment_slots)
"""    
    