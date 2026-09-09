"""
Nikolas Praseutsinh
Python Programming 2026
Due: September 15, 2026
Lab 2: Introduction to Python Programming
Write a Python Program that uses turtle graphics to draw a flower like shape using squares.
""""
import turtle

t = turtle.Turtle()

def drawSquare():
    #draws a square shape using 4 sides
    for i in range(4):
        #move the turtle forward by 100 units
        t.forward(100)
        #turn the turtle right by 90 degrees
        t.right(90)

def drawFlower(numSquares):
    #draws a flower shape using squares
    for i in range(numSquares):
        #call the drawSquare function to draw a square
        drawSquare()
        #turn the turtle right by 360/numSquares degrees to create a flower shape
        t.right(360 / numSquares)

drawFlower(9)

