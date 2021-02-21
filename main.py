######################################
####### Import Python Modules ########
######################################
import os, time, signal
import numpy as np


######################################
######## Import Local Scripts ########
######################################
import board, ball
import paddle, game_over
import bricks
from gletch import _getChUnix as getChar
from alarmexception import AlarmException

######################################
########## Global Variables ##########
######################################
ROWS = 70
COLS = 25
FPS = 5
t = 0.2
MAX_LIVES = 3


######################################
############# Take Input #############
######################################
def alarm_handler(signum, frame):
	raise AlarmException

# get input char
def input_char(timeout):
	signal.signal(signal.SIGALRM, alarm_handler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		txt = getChar()()
		signal.alarm(0)
		return txt
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''
######################################
def end_game():
	exit(0)

Fresh_Board = []
for i in range(COLS):
	temp = []
	for j in range(ROWS):
		temp.append("*")
	Fresh_Board.append(temp)


Balls = []

Paddle = paddle.Paddle(20, 1, 12)
ball_spawn = Paddle.x + np.random.randint(Paddle.lenght)
Balls.append(ball.Ball(ball_spawn, 22, 1,1))
present_lives = MAX_LIVES

Balls[0].attached = True

# exit(0)
present_board = Fresh_Board
Bricks = bricks.create_bricks(10)
for i in Bricks:
	present_board = i.display(present_board)

while True:

	while present_lives:
		inp = input_char(timeout=t/2)
		if( inp != None ):
			time.sleep(t/2)
		if (inp =='d'):
			if (not(Paddle.x+Paddle.lenght >= 70)):
				present_board = Paddle.move(1,present_board)
				ball_spawn += Paddle.v_x
		if (inp =='a'):
			if not (Paddle.x <= 0):
				present_board = Paddle.move(-1,present_board)
				ball_spawn -= Paddle.v_x
		if (inp=='p'):
			Balls[0].attached = False
		if(inp=='q'):
			end_game()

		next_block = present_board[Balls[0].x + Balls[0].v_x][Balls[0].y + Balls[0].v_y]
		if( (next_block == "3") or (next_block == "2") or (next_block == "1")):
			bricks.Brick_collision(Bricks, Balls[0].x, Balls[0].y, Balls[0].v_x, Balls[0].v_y )

		if (Balls[0].attached == False):
			present_board =  Balls[0].move(present_board, Paddle.x + Paddle.lenght//2, Paddle.v_x)
		else:
			present_board = Balls[0].move_with_paddle(present_board, ball_spawn, Paddle.v_x)

		if(present_board == "OVER"):
			print("boom")
			present_lives -= 1
			Balls = []
			ball_spawn = Paddle.x + np.random.randint(Paddle.lenght)
			Balls.append(ball.Ball(ball_spawn, 22, 1,1))
			Balls[0].attached = True
			present_board = Fresh_Board

		os.system("clear")
		os.system("clear")
		print("Lives: ", present_lives)
		board.display_board(present_board)

	
	game_over.GO()


