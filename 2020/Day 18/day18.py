puzzleInput = open('day18input.txt').read().strip().split('\n')


for line in puzzleInput: 
    evalExpressions = []

    # Get all parentheses expressions
    leftParenPos = line.find('(')
    newLine = line
    while(leftParenPos >= 0):
        evalExpressions.append(line[leftParenPos:])
        newLine = newLine[leftParenPos + 1:]
        leftParenPos = newLine.find('(')

    print(evalExpressions)