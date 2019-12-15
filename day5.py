
def pad(positions, length):
    while len(positions) < length:
        positions = '0' + positions
    return positions

def parse(data, input):
    i = 0;
    inp = 0
    output = []
    while i < len(data):
        instruction = data[i]
        command = instruction % 100
        positions = str(instruction // 100)
        if command == 99:
            break
        if command == 1:
            positions = pad(positions, 3)
            curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
            curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
            location = data[i + 3]
            data[location] = curr1 + curr2
            i += 4
        elif command == 2:
            positions = pad(positions, 3)
            curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
            curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
            location = data[i + 3]
            data[location] = curr1 * curr2
            i += 4
        elif command == 3:
            location = data[i + 1]
            data[location] = input[inp]
            inp += 1
            i += 2
        elif command == 4:
            positions = pad(positions, 1)
            output.append(data[data[i + 1]] if positions[0] == '0' else data[i + 1])
            i += 2
        elif command == 5:
            positions = pad(positions, 2)
            curr = data[data[i + 1]] if positions[1] == '0' else data[i + 1]
            if curr != 0:
                i = data[data[i + 2]] if positions[0] == '0' else data[i + 2]
            else:
                i += 3
        elif command == 6:
            positions = pad(positions, 2)
            curr = data[data[i + 1]] if positions[1] == '0' else data[i + 1]
            if curr == 0:
                i = data[data[i + 2]] if positions[0] == '0' else data[i + 2]
            else:
                i += 3
        elif command == 7:
            positions = pad(positions, 3)
            curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
            curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
            location = data[i + 3]
            data[location] = 1 if curr1 < curr2 else 0
            i += 4
        elif command == 8:
            positions = pad(positions, 3)
            curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
            curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
            location = data[i + 3]
            data[location] = 1 if curr1 == curr2 else 0
            i += 4

    return output

data = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,78,5,225,1,166,139,224,101,-74,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1002,136,18,224,101,-918,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,83,84,224,1001,224,-139,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,55,20,225,1101,53,94,225,2,217,87,224,1001,224,-2120,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,102,37,14,224,101,-185,224,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1101,8,51,225,1102,46,15,225,1102,88,87,224,1001,224,-7656,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,29,28,225,1101,58,43,224,1001,224,-101,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1101,93,54,225,101,40,191,224,1001,224,-133,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,40,79,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,434,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,494,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,7,677,677,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,644,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]

print(parse(data, [5]))


