puzzleInput = open('day13input.txt').read().strip().split('\n')

departTime = int(puzzleInput[0])
ids = puzzleInput[1].split(',')
idMults = []

# Part 1
for id in ids: 
    if id == 'x':
        continue

    else:
        id = int(id)

        # Generate closest multiple of id to target departure time
        mult = 1
        currProduct = 0
        while(currProduct < departTime):
            currProduct = id * mult

            if currProduct <= departTime:
                mult = mult + 1
        
        idMults.append((id, mult))

minWait = -1
minID = 0
for item in idMults: 
    if minWait == -1 or item[1] < minWait:
        minWait = item[1]
        minID = item[0]
        
minDepartTime = minID * minWait
diff = minDepartTime - departTime
answer = minID * diff
print(answer)


# Part 2
startID = int(ids[0])
t = startID
incAmount = startID
currTimeMult = 1
busesChecked = 1
busesToCheck = 2

while(busesToCheck <= len(ids)):
    validT = False

    while(validT is False):
        t = t + incAmount
        offset = 1 
        validT = True

        for i in range(1, busesToCheck):

            if(ids[i] == 'x'):
                offset = offset + 1
                continue

            currID = int(ids[i])

            if (t+offset) % currID != 0:
                validT = False
                break

            offset = offset + 1

        currTimeMult = currTimeMult + 1


    if ids[busesToCheck - 1] != 'x': 
        incAmount = incAmount * int(ids[busesToCheck - 1])
    busesToCheck = busesToCheck + 1

print(t)


