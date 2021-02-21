import time

class Ball:

	def __init__ (self, x, y, v_x, v_y):
		super().__init__()
		self.x = x
		self.y = y
		self.v_x = v_x
		self.v_y = v_y
		self.attached = False
		self.spawn = 0

	def update_position(self):
		self.x += self.v_x
		self.y += self.v_y
		if(self.x >= 70):
			self.x -= self.v_x
			self.v_x *= -1
		if (self.x < 0):
			self.x -= self.v_x
			self.v_x *= -1
		if (self.y < 0):
			self.y -= self.v_y
			self.v_y *= -1
		if (self.y >= 25):
			self.y -= self.v_y
			return "OVER"



	def move(self, board, paddle_mid, paddle_vel):
		print(self.y, self.x)
		# time.sleep(0.3)
		board[self.y][self.x] = "."
		if (self.update_position() != "OVER" ):
			if (board[self.y][self.x] == "_" and self.attached==False):
				return self.paddle_bounce(board)
			# if (board[self.y][self.x] == "_" and self.attached==True):
				# return self.move_with_paddle(board, paddle_mid, paddle_vel)
			else:
				board[self.y][self.x] = "0"
			return board
		else:
			return "OVER"

	def paddle_bounce(self,board):
		self.x -= self.v_x
		self.y -= self.v_y
		self.v_y *= -1
		board[self.y][self.x] = "."
		return board

	def move_with_paddle(self, board, paddle_mid, paddle_vel):
		self.y = 22
		if (self.y > 0):
			self.v_y *= -1
		print(self.v_y)
		board[self.y][self.x] = "."
		self.x = paddle_mid
		board[self.y][self.x] = "0"
		return board

