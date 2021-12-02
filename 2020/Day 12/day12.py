import copy

input = open('day12input.txt').read().strip().split('\n')

shipDirections = {
    'N': 0,
    'E': 0,
    'S': 0,
    'W': 0 
}
wayPointDirections = {
    'N': 1,
    'E': 10,
    'S': 0,
    'W': 0 
}

directionNames = ['N', 'E', 'S', 'W']

shipCurrDirection = 'E'
shipCurrDirectionIdx = 1


shipAbsEW = 0
shipAbsNS = 0

# Part 1
for line in input:

    instruction = line[0]
    val = int(line[1:])

    if instruction == 'F':
        shipDirections[currDirection] = shipDirections[currDirection] + val

    elif instruction == 'R':
        offset = val//90
        currDirectionIdx = ((currDirectionIdx + offset) % len(directionNames)) % len(directionNames)
        currDirection = directionNames[currDirectionIdx]
    elif instruction == 'L':
        offset = val//90
        currDirectionIdx = ((currDirectionIdx - offset) % len(directionNames)) % len(directionNames)
        currDirection = directionNames[currDirectionIdx]

    else:
        shipDirections[instruction] = shipDirections[instruction] + val


if shipDirections['N'] > shipDirections['S']:
    absNS = shipDirections['N'] - shipDirections['S']
else:
    absNS = shipDirections['S'] - shipDirections['N']

if shipDirections['E'] > shipDirections['W']:
    absEW = shipDirections['E'] - shipDirections['W']
else: 
    absEW = shipDirections['W'] - shipDirections['E']

print(abs(absNS) + abs(absEW))


# Part 2

def getAbsPosition(directions):
    if directions['N'] > directions['S']:
        absNS = directions['N'] - directions['S']
    else:
        absNS = directions['S'] - directions['N']

    if directions['E'] > directions['W']:
        absEW = directions['E'] - directions['W']
    else: 
        absEW = directions['W'] - directions['E']

    return(absNS, absEW)

def getCurrDirection(directions):
    if directions['N'] >= directions['S']:
        maxNS = 'N'
    else:
        maxNS = 'S'
    
    if directions['E'] >= directions['W']:
            maxEW = 'E'
    else: 
        maxEW = 'W'
    
    return (maxNS, maxEW)


for line in input:
    instruction = line[0]
    val = int(line[1:])

    if instruction == 'F':
        # Get current direction of waypoint
        wayPointNS, wayPointEW = getCurrDirection(wayPointDirections)
        wayPointNSVal, wayPointEWVal = getAbsPosition(wayPointDirections)

        shipDirections[wayPointNS] = shipDirections[wayPointNS] + (val * wayPointNSVal)
        shipDirections[wayPointEW] = shipDirections[wayPointEW] + (val * wayPointEWVal) 

    
    elif instruction == 'R':
        offset = val//90

        oldDirections = copy.deepcopy(wayPointDirections)

        if offset == 1:
            wayPointDirections['N'] = oldDirections['W']
            wayPointDirections['E'] = oldDirections['N']
            wayPointDirections['S'] = oldDirections['E']
            wayPointDirections['W'] = oldDirections['S']

        elif offset == 2: 
            wayPointDirections['S'] = oldDirections['N']
            wayPointDirections['W'] = oldDirections['E']
            wayPointDirections['N'] = oldDirections['S']
            wayPointDirections['E'] = oldDirections['W']

        elif offset == 3:
            wayPointDirections['W'] = oldDirections['N']
            wayPointDirections['N'] = oldDirections['E']
            wayPointDirections['E'] = oldDirections['S']
            wayPointDirections['S'] = oldDirections['W']
        
    
    elif instruction == 'L':

        offset = val//90

        oldDirections = copy.deepcopy(wayPointDirections)

        if offset == 1:
            wayPointDirections['W'] = oldDirections['N']
            wayPointDirections['S'] = oldDirections['W']
            wayPointDirections['E'] = oldDirections['S']
            wayPointDirections['N'] = oldDirections['E']

        elif offset == 2: 
            wayPointDirections['N'] = oldDirections['S']
            wayPointDirections['E'] = oldDirections['W']
            wayPointDirections['S'] = oldDirections['N']
            wayPointDirections['W'] = oldDirections['E']

        elif offset == 3:
            wayPointDirections['E'] = oldDirections['N']
            wayPointDirections['N'] = oldDirections['W']
            wayPointDirections['W'] = oldDirections['S']
            wayPointDirections['S'] = oldDirections['E']
    

    else:
        wayPointDirections[instruction] = wayPointDirections[instruction] + val


absNS, absEW = getAbsPosition(shipDirections)
print(abs(absNS) + abs(absEW))