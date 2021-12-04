import numpy as np 

inp = open('input.txt').read().split('\n')
drawn_nums = [int(i) for i in inp[0].split(',')]

boards = []
currBoard = [[] for i in range(5)]
rowCount = 0 

for line in inp[1:]:
    
    if line.strip() == '':
        continue
    for dig in line.split(' '):
        if dig != '':
            currBoard[rowCount].append(int(dig))
    rowCount += 1

    if rowCount >= 5:
        boards.append(currBoard)
        currBoard = [[] for i in range(5)]
        rowCount = 0

turns_to_win = [-1 for i in range(len(boards))]

#total_min_turns = -1
total_max_turns = -1
best_board = []

for board in boards:
    
    # Replace each digit on board with the turn it was called if it's valid,
    # x if it is not
    new_board = [[0 for i in range(len(board[i]))] for i in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in drawn_nums:
                new_board[i][j] = drawn_nums.index(board[i][j])
            else:
                new_board[i][j] = 'x'
    

    # Get validity of new_board, record lowest number of turns needed to make a row/col valid
    min_turns = -1
    # Find minimum valid turns for row
    for i in range(len(new_board)):
        if not 'x' in new_board[i]:
            turns = max(new_board[i])
            if min_turns == -1 or turns < min_turns:
                min_turns = turns
        #print('turns for row',i,turns)
        
    # Find minimum valid turns for column 
    flipped = np.transpose(new_board)
    for i in range(len(flipped)):
        if not 'x' in flipped[i]:
            turns = max(flipped[i])
            if min_turns == -1 or turns < min_turns:
                min_turns = turns
        #print('turns for col',i,turns)

    #print(min_turns)
    # Compare to total min_turns
    if min_turns != -1 and (total_max_turns == -1 or min_turns > total_max_turns):
        total_max_turns = min_turns
        best_board = board
    
print(total_max_turns)
print(best_board)
unmarked_sum = 0

# Process winning board
for i in range(len(best_board)):
    for j in range(len(best_board[i])):
        # If number came after min turns to win, it is unmarked
        if best_board[i][j] not in drawn_nums or drawn_nums.index(best_board[i][j]) > total_max_turns:
            unmarked_sum += best_board[i][j]

print(unmarked_sum * drawn_nums[total_max_turns])

