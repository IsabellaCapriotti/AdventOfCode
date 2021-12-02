import copy

puzzleInput = open('day17input.txt').read().strip().split('\n')

# Get input as 2D array 
for i, line in enumerate(puzzleInput):
    puzzleInput[i] = list(line)

# Empty dimension
emptyDim = [['.' for i in range(len(puzzleInput[0]))] for j in range(len(puzzleInput))]

# Add to 3D array of cubes
cubes = {}
cubes[0] = copy.deepcopy(puzzleInput)
print(cubes)

# Function to check adjacent points to the passed point
# Retunrs true if point should be active next turn, and false
# if it should be inactive
def checkAdjacentPoints(x, y, z, cubes):
    pointsToCheck = []

    pointsToCheck.append((x, y+1, z+1))
    pointsToCheck.append((x, y-1, z-1))
    pointsToCheck.append((x, y+1, z-1))
    pointsToCheck.append((x, y-1, z+1))
    pointsToCheck.append((x+1, y, z+1))
    pointsToCheck.append((x-1, y, z-1))
    pointsToCheck.append((x+1, y, z-1))
    pointsToCheck.append((x-1, y, z+1))
    pointsToCheck.append((x+1, y+1, z))
    pointsToCheck.append((x-1, y-1, z))
    pointsToCheck.append((x+1, y-1, z))
    pointsToCheck.append((x-1, y+1, z))
    pointsToCheck.append((x+1, y+1, z+1))
    pointsToCheck.append((x-1, y-1, z-1))
    pointsToCheck.append((x+1, y-1, z-1))
    pointsToCheck.append((x-1, y+1, z-1))
    pointsToCheck.append((x-1, y-1, z+1))
    pointsToCheck.append((x-1, y+1, z+1))
    pointsToCheck.append((x+1, y-1, z+1))
    pointsToCheck.append((x+1, y+1, z-1))
    pointsToCheck.append((x, y, z+1))
    pointsToCheck.append((x, y, z-1))
    pointsToCheck.append((x, y+1, z))
    pointsToCheck.append((x, y-1, z))
    pointsToCheck.append((x+1, y, z))
    pointsToCheck.append((x-1, y, z))

    activeCount = 0
        
    # Count all points that are active out of the points to check
    for point in pointsToCheck: 
        pointX = point[0]
        pointY = point[1]
        pointZ = point[2]

        if cubes[pointZ][pointY][pointX] == '#':
            activeCount = activeCount + 1

    
    # Logic for updating state of passed cell
    if cubes[z][y][x] == '#':
        if (activeCount == 2 or activeCount == 3): 
            return True
        else:
            return False

    elif cubes[z][y][x] == '.' and activeCount == 3:
        return True
    else:
        return False
    
for i in range(6): 
    newCubes = copy.deepcopy(cubes)

    # Append new dimensions
    newCubes[-i - 1] = copy.deepcopy(emptyDim)
    newCubes[i + 1] = copy.deepcopy(emptyDim)
    
    for dimension in cubes: 
        currDim = cubes[dimension]
        nextDim = copy.deepcopy(currDim)

        # For each current dimension, check and update all points
        # holy shit
        for i in range(len(currDim)):
            for j in range(len(currDim[i])): 
                checkRes = checkAdjacentPoints(j, i, dimension, newCubes)

                if checkRes is True:
                    nextDim[dimension][i][j] = '#'
                else:
                    nextDim[dimension][i][j] = "."                    
   



    