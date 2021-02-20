######################################
####### Import Python Packages #######
######################################
import os, time
import numpy as np

######################################
######## Import Local Scripts ########
######################################
import board, ball

######################################
########## Global Variables ##########
######################################
ROWS = 70
COLS = 25
FPS = 5

Fresh_Board = []
for i in range(COLS):
	temp = []
	for j in range(ROWS):
		temp.append("*")
	Fresh_Board.append(temp)


Balls = []

Balls.append(ball.Ball(12, 3, 1,1))

while True:
	present_board = Fresh_Board
	time.sleep(1/FPS)
	os.system("clear")
	os.system("clear")


	for i in Balls:
		present_board =  i.move(present_board)

	board.display_board(present_board)