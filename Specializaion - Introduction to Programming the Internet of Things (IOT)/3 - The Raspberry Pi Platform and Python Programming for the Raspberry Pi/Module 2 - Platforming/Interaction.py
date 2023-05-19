#Interaction

'''Scale Widget'''
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w.pack()
#Draws a scale widget
#Slider can be moved by the user

'''Interacting with the Widget'''
#Want to do something when the user moves the slider
w = Scale(master, from_=0, to=100, orient=HORIZONTAL,
    command = update)

def update(duty) :
    pwm.ChangeDutyCycle(float(duty))

#Update function is called
