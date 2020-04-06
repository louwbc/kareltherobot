from env import Environment
from boards import initBoard
from lang import Lang

env = Environment(initBoard, exit, .3)
brd = env.board
env.printBoard()
mini_lang = Lang(env, 'IF front-is-clear THEN move')