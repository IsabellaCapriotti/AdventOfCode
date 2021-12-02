puzzleInput = open('day14input.txt').read().strip().split('\n')

mem = {}
masksAndInstructions = {}


i = 0

def convertToBinary(decimal, numBits): 
    binaryValue = ''

    for i in range(numBits):
        div = decimal // 2
        rem = decimal % 2

        binaryValue = str(rem) + binaryValue
        decimal = div

    return binaryValue


# Get dictionary of masks and associated instructions
for line in puzzleInput:

    if line.find('mask') != -1:
        currMask = line[line.find('=') + 2:]
        masksAndInstructions[currMask] = []

    else:
        masksAndInstructions[currMask].append(line)


# Part 1
for mask in masksAndInstructions:

    for instruction in masksAndInstructions[mask]: 

        # Get memory address and value from instruction
        memAddress = int(instruction[instruction.find('[') + 1 : instruction.find(']')])
        value = int(instruction[instruction.find('=') + 2:].strip())
        
        # Convert value to 36-bit binary
        binaryValue = convertToBinary(value, 36)

        
        newBinaryValue = ''
        # Compare against bitmask to get new value
        for digit in range(len(mask)): 
            currMaskChar = mask[digit]
            currValChar = binaryValue[digit]

            if (currMaskChar == 'X') or currMaskChar == currValChar:
                newBinaryValue = newBinaryValue + currValChar

            else:
                if currValChar == '0':
                    newBinaryValue = newBinaryValue + '1'
                else:
                    newBinaryValue = newBinaryValue + '0'


        mem[memAddress] = newBinaryValue


# Sum values in memory
sum = 0
for address in mem:
    sum = sum + int(mem[address], 2)


print(sum)


# Part 2
addressesWritten = []

for mask in masksAndInstructions: 
    
    for instruction in masksAndInstructions[mask]: 

        # Get starting memory address in decimal and binary
        startAddrDec = int(instruction[instruction.find('[') + 1 : instruction.find(']')])
        startAddrBin = convertToBinary(startAddrDec, 36)

        # Get value to write
        value = int(instruction[instruction.find('=') + 2:])
        valueBin = convertToBinary(value, 36)

        # Apply bitmask 
        newAddrString = ''
        floatCount = 0
        for i in range(len(mask)): 

            if mask[i] == 'X':
                newAddrString = newAddrString + mask[i]
                floatCount = floatCount + 1
            elif mask[i] == '0':
                newAddrString = newAddrString + startAddrBin[i]
            else:
                newAddrString = newAddrString + '1'

        
        # Generate list of address to overwrite
        # Combinations of floating bits = 2^(# of X's) binary strings
        for i in range(2 ** floatCount):
            currXString = convertToBinary(i, floatCount)

            # Start with original string, replace all X's 
            # with corresponding digits of binary string
            floatString = newAddrString
            newFloatString = ''
            usedChars = 0

            for letter in floatString:
                
                if letter == 'X': 
                    newFloatString = newFloatString + currXString[usedChars]
                    usedChars = usedChars + 1
                else: 
                    newFloatString = newFloatString + letter


            # Overwrite memory address with value
            mem[int(newFloatString, 2)] = value


sum = 0
for address in mem:
    sum = sum + mem[address]

print(sum)

