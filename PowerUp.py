import numpy as np

class PowerUp:

	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.v_y = 0.5
		self.typePW = np.random.randint(2)

	def move(self):
		self.y += self.v_y
		if self.y >= 25:
			self.y -= 24

	def display(self, board):
		if self.y >= 24:
			return board, "Over"
		board[int(self.y)][self.x] = "."
		self.move()
		if (self.y <= 23) :
			if board[int(self.y)][self.x] == "." :
				if(self.typePW==0):
					board[int(self.y)][self.x] = "X"
				elif (self.typePW==1):
					board[int(self.y)][self.x] = "S"
			if board[int(self.y)][self.x] == "_" :
				if self.typePW==0 :
					return board, "X"
				elif self.typePW==1 :
					return board, "S"
			return board, ""
		return board, "Over"

	def shrink_paddle(self, board):
		ans = []
		for i in range(25):
			if i != 23:
				ans.append(board[i])
			else:
				temp = []
				for i in range(70):
					temp.append(".")
				ans.append(temp)
		return ans
