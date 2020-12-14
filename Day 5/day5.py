import math 

# Get input
file = open('day5input.txt')
input = file.read().strip().split('\n')

seatIds = []

for line in input:
    low = 0
    high = 128
    mid = 0

    # Get row 
    for character in line[:7]:
        mid = math.ceil( (low + high) / 2)

        if character == 'F':
            high = mid - 1
        else:
            low = mid
    
    row = high

    low = 0
    high = 7 
    mid = 0


    # Get column
    for character in line[7:]:
        mid = math.ceil( (low + high) / 2)

        if character == 'L':
            high = mid - 1
        else:
            low = mid

    col = high

    seatIds.append((row * 8) + col)

# Part 1
print(max(seatIds))

# Part 2
# Sort seat ids
seatIds.sort()
myId = 0

for i, id in enumerate(seatIds):

    if i == 0 or i == len(seatIds) - 1:
        continue
    
    if seatIds[i+1] - id > 1:
        myId = id + 1
        break

    elif id - seatIds[i-1] > 1:
        myId = id - 1
        break

print(myId)