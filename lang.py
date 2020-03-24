class Lang():
    def __init__():
        pass

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
        pass