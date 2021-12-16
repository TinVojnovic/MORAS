def _parse_macro(self):
    #counter za linije
    o = 0
    t = []
    mparams = []
    
    #idemo liniju po liniju i trazimo simbol $
    for line in self._file.split("\n"):

        #idemo kroz liniju ukoliko je veca od 0(tj nije \n) i pocinje sa simbolom $
        if len(line) > 0 and line[0] == "$":

            #$END nam sluzi za while petlju
            if line == "$END":
                if len(t) == 0:
                    self._flag = False
                    self._line = o
                    self._errm = "Invalid macro"
                else:
                    self._file = self._file.replace(
                        line, self._end_while(t[-1]), 1)
                    t.pop(-1)
                    mparams.pop(-1)
            else:
                #rastavljamo line po makro komandi i parametrima
                s = line.split("(")
                comm = s[0][1:].replace(" ", "")
                params = s[1][:-1]
                params = params.split(",")

                #potivamo prikladni makro
                if comm == "MV":
                    self._file = self._file.replace(
                        line, self._mv(params[0], params[1]), 1)
                elif comm == "SWP":
                    self._file = self._file.replace(
                        line, self._swp(params[0], params[1]), 1)
                elif comm == "SUM":
                    self._file = self._file.replace(
                        line, self._sum(params[0], params[1], params[2]), 1)
                elif comm == "WHILE":
                    t.append(o)
                    mparams.append(params[0])
                    self._file = self._file.replace(
                        line, self._while(params[0], o), 1)
                else:
                    self._flag = False
                    self._line = o
                    self._errm = "Invalid macro"
        o += 1


def _while(self, A, o):
    return f"(WHILELOOP{o})\n@{A}\nD=M\n@END_WHILELOOP{o}\nD;JEQ\n"


def _end_while(self, A):
    return f"@WHILELOOP{A}\n0;JMP\n(END_WHILELOOP{A})"


def _mv(self, A, B):
    return f"@{A}\nD=M\n@{B}\nM=D"


def _swp(self, A, B):
    return f"@{A}\nD=M\n@temp\nM=D\n@{B}\nD=M\n@{A}\nM=D\n@temp\nD=M\n@{B}\nM=D\n"


def _sum(self, A, B, C):
    return f"@{A}\nD=M\n@{B}\nD=D+M\n@{C}\nM=D\n"
