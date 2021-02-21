class Paddle:

	def __init__(self, x, v_x, lenght):
		super().__init__()
		self.x = x
		self.y = 3
		self.v_x = 1
		self.lenght = lenght

	def move(self, direction, board):
		for i in range(self.lenght):
			board[3][self.x + i] = "*"
		self.x += direction*self.v_x
		for i in range(self.lenght):
			board[3][self.x + i] = "="
		return board

		