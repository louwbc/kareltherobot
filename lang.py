class Lang():
    def __init__(self, env, source):
        self.env = env
        self.conditions = env.conditions
        self.words = source.split()        # Make prog a list of words
        self.lookup = {}                   # for defined words


    def consume(self, what):
        word = self.getword()
        if word == what:
            return True
        else:
            self.exit('Expecting %s' % what)


    def exit(self, mesg):
        import sys
        trace = '<%s>' % ' '.join(self.ahead)
        if mesg:
            print 'Fatal error: %s %s' % (mesg, trace)
        sys.exit()


    def getInstruction(self):
        word = self.getword()
        if word == 'EOF':
            return 'EOF'
        if word == 'BEGIN':
            insts = []
            while self.nextword() != 'END':
                inst = self.getInstruction()
                if inst:
                    insts.append(inst)
            self.consume('END')
            return insts
        elif word == 'DEFINE-NEW-INSTRUCTION':
            name = self.getword()
            self.consume('AS')
            inst = self.getInstruction()
            self.lookup[name] = inst
            return None
        elif word == 'ITERATE':
            times = int(self.getword())
            self.consume('TIMES')
            inst = self.getInstruction()
            return ['ITERATE', times, inst]
        elif word == 'WHILE':
            cond = self.getword()
            self.consume('DO')
            inst = self.getInstruction()
            return ['WHILE', cond, inst]
        elif word == 'IF':
            cond = self.getword()
            self.consume('THEN')
            inst1 = self.getInstruction()
            if self.nextword() != 'ELSE':
                return ['IF', cond, inst1, None]
            self.consume('ELSE')
            inst2 = self.getInstruction()
            return ['IF', cond, inst1, inst2]
        else:
            return self.lookup.get(word,word)       # change if it was redefined


    def execInstruction():
        if not inst:
            return
        if inst == 'move':
            self.env.move()
        elif inst == 'turnleft':
            self.env.turnleft()
        elif inst == 'pickbeeper':
            self.env.pickbeeper()
        elif inst == 'putbeeper':
            self.env.putbeeper()
        elif inst == 'turnoff':
            self.exit(None)
        elif inst == '':
            pass
        elif inst[0] == 'IF':          # IF cond THEN ... [ELSE ...]
            if self.conditions[inst[1]](self.env):
                self.execInstruction(inst[2])
            elif inst[3]:
                self.execInstruction(inst[3])    # optional ELSE
            elif inst[0] == 'ITERATE':           # ITERATE times ...
                for i in range(inst[1]):
                    self.execInstruction(inst[2])
            elif inst[0] == 'WHILE':             # WHILE cond DO ...
                while self.conditions[inst[1]](self.env):
                    self.execInstruction(inst[2])
            elif type(inst) == type([]):         # BEGIN ... END
                for subInst in inst:
                    self.execInstruction(subInst)
            else:
                self.exit('Illegal instruction: %s' % inst)


    def getword(self):
        if not self.words:
            return 'EOF'
        self.ahead = self.words[:6]        # for error message
        word = self.words.pop(0)
        return word


    def nextword(self):
        if self.words:
            return self.words[0] 
        else:
            return None