from env import Environment
from boards import initBoard

env = Environment(initBoard, exit, .3)
brd = env.board
env.printBoard()