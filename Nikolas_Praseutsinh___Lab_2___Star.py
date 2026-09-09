"""
Nikolas Praseutsinh
Python Programming 2026
Due: September 15, 2026
Lab 2: Introduction to Python Programming
Write a function to make the turtle draw a five-pointed star.
"""

import turtle

t = turtle.Turtle()

def draw_star(size):
    #draws five lines to create a five-pointed star
    for i in range(5):
        #move the turtle forward with a specified size
        t.forward(size)
        #turn the turtle right by 144 degrees to create the star shape
        t.right(144)


draw_star(300)