from copy import copy
from computer import Computer

data = [3,8,1001,8,10,8,105,1,0,0,21,42,51,60,77,94,175,256,337,418,99999,3,9,1001,9,4,9,102,5,9,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99]

comp = Computer([])

curr = 0
for a in range(0, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                for e in range(0, 5):
                    if len(set([a,b,c,d,e])) != 5:
                        continue
                    compA = Computer(copy(data))
                    compB = Computer(copy(data))
                    compC = Computer(copy(data))
                    compD = Computer(copy(data))
                    compE = Computer(copy(data))
                    out, _ = compA.execute([a, 0])
                    out, _ = compB.execute([b, out[0]])
                    out, _ = compC.execute([c, out[0]])
                    out, _ = compD.execute([d, out[0]])
                    out, _ = compE.execute([e, out[0]])
                    curr = max(curr, out[0])

print("ans1: " + str(curr))

curr = -1
for a in range(5, 10):
    for b in range(5, 10):
        for c in range(5, 10):
            for d in range(5, 10):
                for e in range(5, 10):
                    if len(set([a,b,c,d,e])) != 5:
                        continue
                    out = [0]
                    tmp = 0

                    # Initialize 5 computers.
                    compA = Computer(copy(data))
                    compB = Computer(copy(data))
                    compC = Computer(copy(data))
                    compD = Computer(copy(data))
                    compE = Computer(copy(data))

                    # Give them their original parameters.
                    compA.execute([a])
                    compB.execute([b])
                    compC.execute([c])
                    compD.execute([d])
                    compE.execute([e])

                    # Keep feeding new params until it halts.
                    halted = False
                    while not compE.halted:
                        out, halted = compA.execute([out[0]])
                        out, halted = compB.execute([out[0]])
                        out, halted = compC.execute([out[0]])
                        out, halted = compD.execute([out[0]])
                        out, halted = compE.execute([out[0]])
                    curr = max(curr, out[0])

print("ans2: " + str(curr))
