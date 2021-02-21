import numpy as np


class Brick:

	def __init__ (self, x, y, strength):
		super().__init__()
		self.x = x
		self.y = y
		self.strength = strength

	def display(self, board):
		if (self.strength!= 0):
			if (self.strength==1 or self.strength==2 or self.strength==3):
				board[self.y][self.x] = str(self.strength)
			else:
				board[self.y][self.x] = "N"
		return board


def create_bricks(num):
	final = []
	for i in range(num):
		strength_temp = np.random.randint(4)+1
		if (strength_temp==4):
			strength_temp = np.inf
		final.append(Brick(np.random.randint(70),np.random.randint(18), strength_temp ))
	return final


def Brick_collision(list_in, x, y, v_x, v_y):
	for i in list_in:
		if (i.x == x+v_x) and (i.y==y+v_y):
			i.strength -= 1
		else:
			pass
	return list_in
