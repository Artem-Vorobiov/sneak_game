# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os
import time

# Set up the Screen
# def screen_here():
# 	global wn
# 	global pen

# 	pen = turtle.Turtle()
# 	pen.hideturtle()

# 	wn = turtle.Screen()
# 	wn.setup(width=0.7, height = 0.7)
# 	wn.bgcolor('lightgreen')
# 	wn.tracer(3)

class Game():

	def __init__(self):
		self.pen = turtle.Turtle()
		self.wn  = turtle.Screen()

	def screen_here(self):
		self.pen.hideturtle()
		self.wn.setup(width=0.7, height = 0.7)
		self.wn.bgcolor('lightgreen')
		self.wn.tracer(3)

	def drow_border(self):
		self.pen.speed(0)
		self.pen.color('black')
		self.pen.pensize(12)
		self.pen.penup()
		self.pen.goto(-300,300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()
		self.pen.pendown()


game = Game()
game.screen_here()
game.drow_border()



time.sleep(4)