import numpy as np

inp = open('input.txt').read().split('\n')

points = [['.' for i in range(1311)] for j in range(895)]
folds = []
for line in inp:

    if line.strip() == '':
        continue

    if not 'fold' in line: 
        coord = line.split(',')
        points[int(coord[1])][int(coord[0])] = '#'
    
    else: 
        equalIdx = line.find('=')
        folds.append([line[equalIdx-1], int(line[equalIdx+1:])])


for fold in folds:
    dir = fold[0]
    line = fold[1]

    if dir == 'y': 
        currSourceRow = line+1
        currTargetRow = line-1

        while currTargetRow >= 0 and currSourceRow <= len(points)-1: 
            for col in range(len(points[currSourceRow])):
                if points[currSourceRow][col] == '#':
                    points[currTargetRow][col] = '#'
            currTargetRow -= 1
            currSourceRow += 1

        points = points[:line]

    elif dir == 'x':
        currSourceCol = line+1
        currTargetCol = line-1 

        while currTargetCol >= 0 and currSourceCol <= len(points[0])-1: 
            for row in range(len(points)):
                if points[row][currSourceCol] == '#': 
                    points[row][currTargetCol] = '#'
            currTargetCol -= 1
            currSourceCol += 1

        for i in range(len(points)):
            points[i] = points[i][:line]


trueCount = 0 

# for i in range(len(points)):
#     for j in range(len(points[i])):
#         if points[i][j] == '#':
#             trueCount += 1

# print(trueCount)
print(np.array(points))
