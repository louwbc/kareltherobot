from env import Environment
from boards import initBoard

env = Environment(initBoard, exit, .3)
brd = env.board
env.printBoard()

print "start test move"
env.move()

print "start test turnleft"
env.turnleft()

print "start test move twice"
env.move()
env.move()

print "start test turenleft three time"
env.turnleft()
env.turnleft()
env.turnleft()

print "start test move 3 times"
env.move()
env.move()
env.move()

print "start pick beeb"
env.pickbeeper()

print "start turnleft"
env.turnleft()

print "start move 2 time"
env.move()
env.move()

print "start test putbeeper"
env.putbeeper()

print "move"
env.move()

print "test cond"
env.test('front-is-clear')

print "test move blocked"
env.turnleft()
env.move()

print "test done"