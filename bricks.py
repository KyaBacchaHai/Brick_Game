import numpy as np
import time

class Brick:

	def __init__ (self, x, y, strength):
		super().__init__()
		self.x = x
		self.y = y
		self.strength = strength

	def display(self, board):
		if (self.strength==1 or self.strength==2 or self.strength==3):
			board[self.y][self.x] = str(self.strength)
		elif (self.strength==0) :
			board[self.y][self.x] = "*"
		elif (self.strength == 5):
			board[self.y][self.x] = "E"
		else:
			board[self.y][self.x] = "N"
		return board


def create_bricks(num):
	final = []
	while num:
		# 1: normal
		# 2: normal
		# 3: normal
		# 4: inf
		# 5: explode
		strength_temp = np.random.randint(5)+1
		x_temp = np.random.randint(70)
		y_temp = np.random.randint(18)
		if (strength_temp==4):
			strength_temp = np.inf
		true_false = True
		for i in final:
			if (i.x == x_temp) and (i.y == y_temp):
				true_false = False
		if true_false:
			final.append(Brick(x_temp, y_temp, strength_temp ))
			num -= 1
	return final


def Brick_collision(list_in, x, y, v_x, v_y):
	for i in list_in:
		if (i.x == x+v_x) and (i.y==y+v_y):
			i.strength -= 1
		else:
			pass
	return list_in


def Explode(list_in, x_f, y_f):
	for i in range(-1,2):
		for j in range(-1,2):
			for ele in list_in:
				if ((ele.x == x_f + i) and (ele.y == y_f + j) ):
					ele.strength = 0
	return list_in
