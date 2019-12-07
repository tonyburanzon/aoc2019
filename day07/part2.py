"""
--- Part Two ---

It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a feedback loop:

      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)

Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop: the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be sent to the thrusters using the new phase settings and feedback loop arrangement.

Here are some example programs:

    Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5

    Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

    3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10

Try every combination of the new phase settings on the amplifier feedback loop. What is the highest signal that can be sent to the thrusters?

Your puzzle answer was 5406484.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
from itertools import permutations

s = []
with open("input", "r") as f:
    s = f.read()
    s = s[:-1]
    s = s.split(",")
    s = [int(x) for x in s]

def amp(string, in_val, op_ptr):
    i = 0
    while op_ptr < len(string):
        opcode = string[op_ptr] % 100
        mode1 = string[op_ptr] // (10 ** 2) % 10
        mode2 = string[op_ptr] // (10 ** 3) % 10
        mode3 = string[op_ptr] // (10 ** 4) % 10
        if opcode == 99:
            return ("HALT", "HALT")
            quit()

        elif opcode == 1:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            string[string[op_ptr + 3]] = op1 + op2
            op_ptr += 4

        elif opcode == 2:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            string[string[op_ptr + 3]] = op1 * op2
            op_ptr += 4

        elif opcode == 3:
            string[string[op_ptr + 1]] = in_val[i]
            i += 1
            op_ptr += 2

        elif opcode == 4:
            ret = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            return (ret, op_ptr + 2)

        elif opcode == 5:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            op_ptr = op2 if op1 else op_ptr + 3

        elif opcode == 6:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            op_ptr = op2 if not op1 else op_ptr + 3

        elif opcode == 7:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            string[string[op_ptr + 3]] = 1 if op1 < op2 else 0
            op_ptr += 4

        elif opcode == 8:
            op1 = string[op_ptr + 1] if mode1 else string[string[op_ptr + 1]]
            op2 = string[op_ptr + 2] if mode2 else string[string[op_ptr + 2]]
            string[string[op_ptr + 3]] = 1 if op1 == op2 else 0
            op_ptr += 4

        else:
            print("Something went wrong")
            quit()


def find_max():
    perm = permutations([5,6,7,8,9])
    outputs = []
    for p in perm:
        output = 0
        in2 = ""
        string1 = s.copy()
        string2 = s.copy()
        string3 = s.copy()
        string4 = s.copy()
        string5 = s.copy()
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        ptr4 = 0
        ptr5 = 0
        in2, ptr1 = amp(string1, (p[0], 0), ptr1)
        in3, ptr2 = amp(string2, (p[1], in2), ptr2)
        in4, ptr3 = amp(string3, (p[2], in3), ptr3)
        in5, ptr4 = amp(string4, (p[3], in4), ptr4)
        output, ptr5 = amp(string5, (p[4], in5), ptr5)

        while 1:
            in2, ptr1 = amp(string1, (output,), ptr1)
            if in2 == "HALT": break
            in3, ptr2 = amp(string2, (in2,), ptr2)
            in4, ptr3 = amp(string3, (in3,), ptr3)
            in5, ptr4 = amp(string4, (in4,), ptr4)
            output, ptr5 = amp(string5, (in5,), ptr5)

        outputs.append(output)
    print(max(outputs))
    
find_max()

