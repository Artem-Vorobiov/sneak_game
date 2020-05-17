# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os
import time


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


class Target(turtle.Turtle):

	def __init__(self, shape, color):
		turtle.Turtle.__init__(self)
		self.shape(shape)
		self.color(color)
		self.penup()
		x, y = random.randint(-290, 290), random.randint(-290, 290)
		self.goto(x, y)
		self.pendown()
		self.speed(0)








game = Game()
game.screen_here()
game.drow_border()

target_1 = Target('circle', 'red')

















time.sleep(4)