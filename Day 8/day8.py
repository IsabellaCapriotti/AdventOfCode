import copy

file = open("day8input.txt")
input = file.read().strip().split('\n')

# Part 1 
accumulator = 0 
i = 0 
seenIndeces = []

while(i < len(input)):     
    line = input[i]

    # Get instruction and value
    instruction = line[:line.find(' ')]
    fullValue = line[line.find(' ') + 1:]

    num = int(fullValue[1:])
    if fullValue[0] == '-':
        num = num * -1

    # Check if index has already been visited
    if i in seenIndeces:
        break

    # Add index to scene indeces
    seenIndeces.append(i)

    # Follow instruction
    if instruction == 'acc':
        accumulator = accumulator + num
        i = i + 1
    elif instruction == 'jmp': 
        i = i + num
    else:
        i = i + 1
    

print(accumulator)

# Part 2
def checkLoop(instructions):
    accumulator = 0 
    i = 0 
    seenIndeces = []

    while(i < len(instructions)):     
        line = instructions[i]

        # Get instruction and value
        instruction = line[:line.find(' ')]
        fullValue = line[line.find(' ') + 1:]

        num = int(fullValue[1:])
        if fullValue[0] == '-':
            num = num * -1

        # Check if index has already been visited
        if i in seenIndeces:
            return (False, accumulator)

        # Add index to scene indeces
        seenIndeces.append(i)

        # Follow instruction
        if instruction == 'acc':
            accumulator = accumulator + num
            i = i + 1
        elif instruction == 'jmp': 
            i = i + num
        else:
            i = i + 1
    
    return (True, accumulator) 


for i, line in enumerate(input): 
    # Get instruction and value
    instruction = line[:line.find(' ')]
    fullValue = line[line.find(' ') + 1:]

    num = int(fullValue[1:])
    if fullValue[0] == '-':
        num = num * -1

    # Attempt to change instruction instruction
    if instruction == 'jmp': 
        line = line.replace('jmp', 'nop')    
    elif instruction == 'nop':
        line = line.replace('nop', 'jmp')

    # Check new instruction set for validity
    newInstructions = copy.deepcopy(input)
    newInstructions[i] = line

    (isValid, acc) = checkLoop(newInstructions)

    if isValid is True:
        print(acc)
        



    