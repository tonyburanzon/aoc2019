


def run(prog):
    def parameter(instr, n):
        mode = instr // (10 ** (n + 1)) % 10
        if mode == 0:
            return prog[prog[pc + n]]
        elif mode == 1:
            return prog[pc + n]
        else:
            print("Somethng went wrong")
            quit()
    

    pc = 0
    while pc < len(prog):
        instr = prog[pc]
        opc = instr % 100
        if opc == 99:
            return prog
        
        elif opc == 1:
            prog[prog[pc + 3]] = parameter(instr, 1) + parameter(instr, 2)
            pc+= 4
        
        elif opc == 2:
            prog[prog[pc + 3]] = parameter(instr, 1) * parameter(instr, 2)
            pc+= 4
        
        elif opc == 3:
            prog[prog[pc + 1]] = 5
            pc += 2
        
        elif opc == 4:
            print(parameter(instr, 1))
            pc+= 2
        
        elif opc == 5:
            if parameter(instr, 1):
                pc = parameter(instr, 2)
            else:
                pc+= 3
        
        elif opc == 6:
            if  not parameter(instr, 1):
                pc = parameter(instr, 2)
            else:
                pc+= 3

        elif opc == 7:
            if parameter(instr, 1) < parameter(instr, 2):
                prog[prog[pc + 3]] = 1
            else:
                prog[prog[pc + 3]] = 0
            pc+= 4

        elif opc == 8:
            if parameter(instr, 1) == parameter(instr, 2):
                prog[prog[pc + 3]] = 1
            else:
                prog[prog[pc + 3]] = 0
            pc+= 4
        
def main():
    with open("input", "r") as f:
        prog = [int(part) for part in f.read().strip().split(",")]
        run(prog)

main()
