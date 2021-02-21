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
import bricks, PowerUp
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
TIME_INI = time.time()

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
		temp.append(".")
	Fresh_Board.append(temp)


Balls = []

Paddle = paddle.Paddle(20, 1, 12)
ball_spawn = Paddle.x + np.random.randint(Paddle.lenght)
Balls.append(ball.Ball(ball_spawn, 22, 1,1))
present_lives = MAX_LIVES
present_points = 0
PowerUps = []

Balls[0].attached = True

# exit(0)
present_board = Fresh_Board
Bricks = bricks.create_bricks(100)
for i in Bricks:
	present_board = i.display(present_board)

while True:

	while present_lives:
		game_time = round(time.time() - TIME_INI)
		inp = input_char(timeout=t/2)
		if( inp != None ):
			time.sleep(t/2)
		if (inp =='d'):
			if (Paddle.x + Paddle.v_x + Paddle.lenght <= 69):
				present_board = Paddle.move(1,present_board)
				ball_spawn += Paddle.v_x
		if (inp =='a'):
			if (Paddle.x - Paddle.v_x >= 0):
				present_board = Paddle.move(-1,present_board)
				ball_spawn -= Paddle.v_x
		if (inp=='p'):
			Balls[0].attached = False
		if(inp=='q'):
			end_game()

		for i in PowerUps:
			present_board, string =  i.display(present_board)
			if string == "Over":
				PowerUps.remove(i)
			elif string == "X":
				Paddle.lenght *= 2
				if(Paddle.lenght>=69):
					Paddle.lenght = 69
				if (Paddle.x + Paddle.lenght > 70):
					Paddle.x = 70 - Paddle.lenght - 1
				present_board = Paddle.move(1,present_board)
				present_board = Paddle.move(-1,present_board)
				PowerUps.remove(i)
			elif string == "S":
				Paddle.lenght = Paddle.lenght//2
				present_board = i.shrink_paddle(present_board)
				present_board = Paddle.move(1,present_board)
				present_board = Paddle.move(-1,present_board)
				PowerUps.remove(i)

		if (Balls[0].attached == False):
			try:
				next_block = present_board[Balls[0].y + Balls[0].v_y][Balls[0].x + Balls[0].v_x]
				if( (next_block == "3") or (next_block == "2") or (next_block == "1") or (next_block == "N") ):
					Bricks = bricks.Brick_collision(Bricks, Balls[0].x, Balls[0].y, Balls[0].v_x, Balls[0].v_y )
					present_points += 10
					Balls[0].v_x *= -1
					Balls[0].v_y *= -1
					if (np.random.randint(10) > 1):
						PowerUps.append(PowerUp.PowerUp(Balls[0].x - Balls[0].v_x, Balls[0].y - Balls[0].v_y))
				if (next_block == "E") :
					Balls[0].v_x *= -1
					Balls[0].v_y *= -1
					Bricks = bricks.Explode(Bricks,Balls[0].x - Balls[0].v_x, Balls[0].y - Balls[0].v_y )

				present_board = Fresh_Board
				present_board = Paddle.move(1,present_board)
				present_board = Paddle.move(-1,present_board)
				for i in Bricks:
					present_board = i.display(present_board)
			except:
				pass

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
		print("Points: ", present_points)
		print("Time: ", game_time, "sec")
		board.display_board(present_board)

	
	game_over.GO()


