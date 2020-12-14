# Get input
file = open("day6input.txt")
answers = file.read().strip().split('\n\n')
answerTotal = 0

for group in answers: 
    
    seenAnswers = []
    sharedAnswers = []

    # Go through each line
    lines = group.split('\n')
    
    # Get all characters
    for line in lines:        
        for character in line:
            if character not in seenAnswers: 
                seenAnswers.append(character)
                sharedAnswers.append(character)

    # Check that characters are shared
    for line in lines:
        for character in seenAnswers:
            if character not in line and character in sharedAnswers:
                sharedAnswers.remove(character)
                  
    answerTotal = answerTotal + len(sharedAnswers)

print(answerTotal)
    
    