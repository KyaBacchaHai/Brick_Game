class Paddle:

	def __init__(self, x, v_x, lenght):
		super().__init__()
		self.x = x
		self.y = 23
		self.v_x = 2
		self.lenght = lenght

	def move(self, direction, board):
		for i in range(self.lenght):
			board[self.y][self.x + i] = "*"
		self.x += direction*self.v_x
		for i in range(self.lenght):
			board[self.y][self.x + i] = "_"
		return board

		