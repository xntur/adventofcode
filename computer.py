def pad(positions, length):
    while len(positions) < length:
        positions = '0' + positions
    return positions

class Computer:
    halted = False
    
    def execute(self, data, input):
        self.halted = False
        i = 0;
        inp = 0
        output = []
        while i < len(data):
            instruction = data[i]
            command = instruction % 100
            positions = str(instruction // 100)
            if command == 99:
                self.halted = True
                break
            # Add
            if command == 1:
                positions = pad(positions, 3)
                curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
                curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
                location = data[i + 3]
                data[location] = curr1 + curr2
                i += 4
            # Multiply
            elif command == 2:
                positions = pad(positions, 3)
                curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
                curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
                location = data[i + 3]
                data[location] = curr1 * curr2
                i += 4
            # Read input
            elif command == 3:
                location = data[i + 1]
                data[location] = input[inp]
                inp += 1
                i += 2
            # Output
            elif command == 4:
                positions = pad(positions, 1)
                output.append(data[data[i + 1]] if positions[0] == '0' else data[i + 1])
                i += 2
            # Jump if true
            elif command == 5:
                positions = pad(positions, 2)
                curr = data[data[i + 1]] if positions[1] == '0' else data[i + 1]
                if curr != 0:
                    i = data[data[i + 2]] if positions[0] == '0' else data[i + 2]
                else:
                    i += 3
            # Jump if false
            elif command == 6:
                positions = pad(positions, 2)
                curr = data[data[i + 1]] if positions[1] == '0' else data[i + 1]
                if curr == 0:
                    i = data[data[i + 2]] if positions[0] == '0' else data[i + 2]
                else:
                    i += 3
            # If less than
            elif command == 7:
                positions = pad(positions, 3)
                curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
                curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
                location = data[i + 3]
                data[location] = 1 if curr1 < curr2 else 0
                i += 4
            # If equal to
            elif command == 8:
                positions = pad(positions, 3)
                curr1 = data[data[i + 1]] if positions[2] == '0' else data[i + 1]
                curr2 = data[data[i + 2]] if positions[1] == '0' else data[i + 2]
                location = data[i + 3]
                data[location] = 1 if curr1 == curr2 else 0
                i += 4

    return output
