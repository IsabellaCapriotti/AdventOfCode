import math
import numpy as np  

inp = open('input.txt').read().split('\n')

risks = []
for line in inp:
    new = [int(i) for i in list(line)]
    risks.append(new)

origlenx = len(risks)
origleny = len(risks[0])

# extend all original rows
for j in range(origlenx): 
    start_row = risks[j]
    
    for i in range(1, 5): 

        for k in range(origleny):
            if risks[j][k] + i <= 9: 
                start_row.append(risks[j][k] + i)
            else: 
                start_row.append((risks[j][k] + i) % 9)
                
    risks[j] = start_row
origleny = len(risks[0])

# duplicate down 
for i in range(1, 5): 
    for j in range(origlenx): 
        new_row = []
        for k in range(origleny): 
            if risks[j][k] + i <= 9: 
                new_row.append(risks[j][k] + i)
            else: 
                new_row.append((risks[j][k] + i) % 9)

        risks.append(new_row)
            

# djikstra's algorithm but bad
weights = [[math.inf for j in range(len(risks[i]))] for i in range(len(risks))]
done = [[False for j in range(len(risks[i]))] for i in range(len(risks))]
processing = [[False for j in range(len(risks[i]))] for i in range(len(risks))]

weights[0][0] = 0 
processing[0][0] = True

def find_smallest(weights, done, processing):
    smallest = -1
    coords = []
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            if processing[i][j] and not done[i][j] and (weights[i][j] < smallest or smallest == -1 ):
                smallest = weights[i][j]
                coords = [i, j]

    return coords


while True:

    curr = find_smallest(weights, done, processing)
    if curr == [] or curr == [len(risks)-1, len(risks[0])-1]:
        print(curr)
        break
    
    # once popped, mark it as done with its final weight
    row = curr[0]
    col = curr[1]
    weight = weights[row][col]

    weights[row][col] = weight
    done[row][col] = True
    processing[row][col] = False

    # add neigbors
    if row > 0 and not done[row-1][col]:

        if processing[row-1][col]:
            new_weight = weight + risks[row-1][col]
            if new_weight < weights[row-1][col]:
                weights[row-1][col] = new_weight
        else:
            processing[row-1][col] = True 
            weights[row-1][col] = weight + risks[row-1][col]

    if row < len(risks)-1 and not done[row+1][col]:

        if processing[row+1][col]:
            new_weight = weight + risks[row+1][col]
            if new_weight < weights[row+1][col]:
                weights[row+1][col] = new_weight
        else:
            processing[row+1][col] = True 
            weights[row+1][col] = weight + risks[row+1][col]

    if col > 0 and not done[row][col-1]:

        if processing[row][col-1]:
            new_weight = weight + risks[row][col-1]
            if new_weight < weights[row][col-1]:
                weights[row][col-1] = new_weight
        else:
            processing[row][col-1] = True 
            weights[row][col-1] = weight + risks[row][col-1]

    if col < len(risks[row])-1 and not done[row][col+1]:

        if processing[row][col+1]:
            new_weight = weight + risks[row][col+1]
            if new_weight < weights[row][col+1]:
                weights[row][col+1] = new_weight
        else:
            processing[row][col+1] = True 
            weights[row][col+1] = weight + risks[row][col+1]


print(weights[len(risks)-1][len(risks)-1])