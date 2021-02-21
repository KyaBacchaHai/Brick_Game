import numpy as np


class Brick:

	def __init__ (self, x, y, strength):
		super().__init__()
		self.x = x
		self.y = y
		self.strength = strength

	def display(self, board):
		if (self.strength!= 0):
			board[self.y][self.x] = str(self.strength)
		return board


def create_bricks(num):
	final = []
	for i in range(num):
		final.append(Brick(np.random.randint(70),np.random.randint(18), np.random.randint(3)+1 ))
	return final


def Brick_collision(list, x, y, v_x, v_y):
	pass