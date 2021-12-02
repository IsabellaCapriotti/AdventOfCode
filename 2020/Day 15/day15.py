startingNumbers = [1, 2, 16, 19, 18, 0]

currNumber = startingNumbers[len(startingNumbers) - 1]
numbersSpoken = {}

# Add starting numbers to numbers spoken
for i in range(len(startingNumbers) - 1):
    num = startingNumbers[i]

    if num not in numbersSpoken:
        numbersSpoken[num] = [i+1]
    
    else:
        numbersSpoken[num].append(i+1)


# For part 1, range would be changed to 2021
for i in range(len(startingNumbers), 30000001): 
    nextNumber = 0 

    # Check if last number has already been spoken 
    if currNumber in numbersSpoken:
        lastTurn = numbersSpoken[currNumber][len(numbersSpoken[currNumber]) - 1]
        nextNumber = i - lastTurn

    # Add next number and turn to spoken numbers
    if currNumber in numbersSpoken:
        numbersSpoken[currNumber].append(i)
    else:
        numbersSpoken[currNumber] = [i]

    prevNumber = currNumber
    currNumber = nextNumber


# Final current number
print(prevNumber)
