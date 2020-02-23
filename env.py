class Environment:
    """The world of Karel """ 
    def __init__(self, text, fatal, interval=.3):
        self.board = text.rstrip().split('\n')
        self.board = filter(lambda x: len(x)>0, self.board)
        self.karelPos = self.karelDir = None
        self.karelBeepers = 0                      # beepers in Karel's bag
        self.beepers = {}                          # squares with beepers
        self.fatal = fatal                         # the exit function
        self.interval = interval                   # the time between moves
        self.nrows = len(self.board)               # rows on the board
        self.ncols = len(self.board[0])            # row 0 must be longest
        self.incr = ((-1,0),(0,1),(1,0),(0,-1))    # for each dirc
        self.conditions = conditions               # boolean tests
        for row in range(self.nrows):
            self.board[row] = list(self.board[row])  # nested lists
            for col in range(self.ncols):
                pos = (row, col)
                c = self.board[row][col]
                kdir = '^>v<'.find(c)              # set Karel's direction by symbol
                if kdir >= 0 :
                    self.karelPos = (row, col)
                    self.karelDir = kdir
                elif ' 123456789'.find(c) > 0:
                    self.beepers[pos] = int(c)     # set # of beepers for pos


    def getSquare(self, dirc):     # dirc relative to kdir
        incr = ((-1,0),(0,1),(1,0),(0,-1))    # for each dirc
        kpos = self.karelPos
        kdir = self.karelDir
        ndir = (kdir+dirc) % 4
        return self.addPos(kpos, self.incr[ndir])

    def isBlocked(self, sqr):
        occu = self.boardGet(sqr)
        return not (occu == '.' or self.beepers.get(sqr))

    def nbrBlocked(self, dirc):
        sqr = self.getSquare(dirc)
        return self.isBlocked(sqr)