file = open("day2input.txt", "r")
input = file.read().split('\n')

validPasswordCount = 0

for passwordSpecs in input: 

    # Extract needed values
    semicolonPos = passwordSpecs.find(':')
    keyLetter = passwordSpecs[semicolonPos - 1:semicolonPos].strip()
    
    keyLetterPos = passwordSpecs.find(keyLetter)
    dashPos = passwordSpecs.find('-')

    minValue = (int)(passwordSpecs[0:dashPos])
    maxValue = (int)(passwordSpecs[dashPos + 1:keyLetterPos - 1])
    
    password = passwordSpecs[semicolonPos + 1:].strip()

    letterMatchCount = 0 

    if password[minValue - 1] == keyLetter:
        letterMatchCount = letterMatchCount + 1
    if password[maxValue - 1] == keyLetter: 
        letterMatchCount = letterMatchCount + 1

    if letterMatchCount == 1: 
        validPasswordCount = validPasswordCount + 1

        


print(validPasswordCount)
            
