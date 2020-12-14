import copy
input = open('day11input.txt').read().strip().split('\n')

for i, line in enumerate(input):
    input[i] = list(line)

nextState = copy.deepcopy(input)

# Part 2 (Logic for part 1 is commented at the bottom!)
changed = True
while changed is True:
    changed = False

    for i in range(len(input)):
        for j in range(len(input[i])):

            # Logic for empty seat
            if input[i][j] == 'L':
                occupiedCount = 0
                emptyCount = 0

                iCount = i
                jCount = j
                check = True
                while iCount > 0 and check is True:
                    if input[iCount-1][jCount] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1

                iCount = i
                jCount = j
                check = True
                
                while iCount > 0 and jCount > 0 and check is True:
                    if input[iCount-1][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1
                    jCount = jCount - 1

                iCount = i
                jCount = j
                check = True
                while iCount > 0 and jCount < len(input[i]) - 1 and check is True:
                    if input[iCount-1][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1
                    jCount = jCount + 1
                
                iCount = i
                jCount = j
                check = True
                while jCount > 0 and check is True:
                    if input[iCount][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    jCount = jCount - 1

                iCount = i
                jCount = j
                check = True
                while jCount < len(input[i]) - 1 and check is True:
                    if input[iCount][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    jCount = jCount + 1

                iCount = i
                jCount = j
                check = True
                while check is True and iCount < len(input) - 1 and jCount > 0:
                    if input[iCount+1][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                    jCount = jCount - 1

                iCount = i
                jCount = j
                check = True
                while check is True and iCount < len(input) - 1:
                    if input[iCount+1][jCount] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                
                iCount = i
                jCount = j
                check = True
                while check is True and iCount < len(input) - 1 and jCount < len(input[i]) - 1:
                    if input[iCount+1][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                    jCount = jCount + 1
                
                # Update next state
                if occupiedCount == 0:
                    changed = True
                    nextState[i][j] = '#'
                    
            # Logic for occupied seat
            elif input[i][j] == '#':
                occupiedCount = 0
                emptyCount = 0

                iCount = i
                jCount = j
                check = True
                while iCount > 0 and check is True:
                    if input[iCount-1][jCount] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1

                iCount = i
                jCount = j
                check = True
                while iCount > 0 and jCount > 0 and check is True:
                    if input[iCount-1][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1
                    jCount = jCount - 1

                iCount = i
                jCount = j
                check = True
                while check is True and iCount > 0 and jCount < len(input[i]) - 1:
                    if input[iCount-1][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount-1][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount - 1
                    jCount = jCount + 1
                
                iCount = i
                jCount = j
                check = True
                while jCount > 0 and check is True:
                    if input[iCount][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    jCount = jCount - 1

                check = True
                iCount = i
                jCount = j
                while jCount < len(input[i]) - 1 and check is True:
                    if input[iCount][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    jCount = jCount + 1

                iCount = i
                jCount = j
                check = True
                while check is True and iCount < len(input) - 1 and jCount > 0:
                    if input[iCount+1][jCount-1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount-1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                    jCount = jCount - 1

                iCount = i
                jCount = j
                check = True
                while iCount < len(input) - 1 and check is True:
                    if input[iCount+1][jCount] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                
                iCount = i
                jCount = j
                check = True
                while check is True and iCount < len(input) - 1 and jCount < len(input[i]) - 1:
                    if input[iCount+1][jCount+1] == '#':
                        occupiedCount = occupiedCount + 1
                        check = False
                    elif input[iCount+1][jCount+1] == 'L':
                        emptyCount = emptyCount + 1
                        check = False
                    iCount = iCount + 1
                    jCount = jCount + 1

                if occupiedCount >= 5: 
                    changed = True
                    nextState[i][j] = 'L'

    # Update board state
    input = copy.deepcopy(nextState)         

# Count occupied seats
occupiedCount = 0 

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            occupiedCount = occupiedCount + 1
print(occupiedCount)



# Logic for Part 1
# if i > 0 and input[i-1][j] == '#':
#     emptyCount = emptyCount + 1
#     if i > 0 and j > 0 and input[i-1][j-1] == '#':
#         emptyCount = emptyCount + 1        
#     if i > 0 and j < len(input[i]) - 1 and input[i-1][j+1] == '#':
#         emptyCount = emptyCount + 1
#     if j > 0 and input[i][j-1] == '#':
#         emptyCount = emptyCount + 1
#     if j < len(input[i]) - 1 and input[i][j+1] == '#':
#         emptyCount = emptyCount + 1
#     if i < len(input) - 1 and j > 0 and input[i+1][j-1] == '#':
#         emptyCount = emptyCount + 1
#     if i < len(input) - 1 and input[i+1][j] == '#':
#         emptyCount = emptyCount + 1
#     if i < len(input) - 1 and j < len(input[i]) - 1 and input[i+1][j+1] == '#':
#         emptyCount = emptyCount + 1

#     if emptyCount >= 4:
#         changed = True
#         nextState[i][j] = 'L'

# # If no occupied seats adjacent, change to occupied
#                 if i > 0 and input[i-1][j] == '#':
#                     occupiedCount = 1
#                 if i > 0 and j > 0 and input[i-1][j-1] == '#':
#                     occupiedCount = 1
#                 if i > 0 and j < len(input[i]) - 1 and input[i-1][j+1] == '#':
#                     occupiedCount = 1
#                 if j > 0 and input[i][j-1] == '#':
#                     occupiedCount = 1
#                 if j < len(input[i]) - 1 and input[i][j+1] == '#':
#                     occupiedCount = 1
#                 if i < len(input) - 1 and j > 0 and input[i+1][j-1] == '#':
#                     occupiedCount = 1
#                 if i < len(input) - 1 and input[i+1][j] == '#':
#                     occupiedCount = 1
#                 if i < len(input) - 1 and j < len(input[i]) - 1 and input[i+1][j+1] == '#':
#                     occupiedCount = 1