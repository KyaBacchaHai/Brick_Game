class Ball:

	def __init__ (self, x, y, v_x, v_y):
		super().__init__()
		self.x = x
		self.y = y
		self.v_x = v_x
		self.v_y = v_y

	def update_position(self):
		self.x += self.v_x
		self.y += self.v_y
		if(self.x >= 70):
			self.x -= self.v_x
		if (self.y >= 25):
			self.y -= self.v_y


	def move(self, board):
		board[self.y][self.x] = "*"
		self.update_position()
		board[self.y][self.x] = "⊙"
		return board
