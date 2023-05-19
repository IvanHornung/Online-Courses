#Tkinter Library

'''Tkinter'''
#Tkinter library provides tools for writing programs that use graphics:
#   -many GUI widgets
#       -buttons, menus, labels, scrollbars, etc.
#   -a canvas widget on which arbitrary drawings can be created
#       -using lines, circles, rectangles, ovals, images, text, etc.

'''Sample Tkinter Program'''
from tkinter import *
root = Tk() #constructor function for the main class in library
root.geometry('800x600') #set the window size
c = Canvas(root, width=800, height=600) #creates a canvas (drawing)
c.pack() #makes canvas appear on screen
r = c.create_rectangle(0, 0, 50, 50, fill='red', outline='red') #draw in canvas
