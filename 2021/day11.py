inp = open('input.txt').read().split('\n')
octopi = []
flashes = 0
for line in inp:
    octopi.append([int(i) for i in list(line)])

def flash(row, col, octopi, flashed, q):
    global flashes
    flashed[row][col] = True
    flashes += 1
    
    if row > 0: 
        octopi[row-1][col] += 1
        if octopi[row-1][col] > 9: 
            q.append([row-1,col])

    if row < len(octopi)-1: 
        octopi[row+1][col] += 1
        if octopi[row+1][col] > 9: 
            q.append([row+1,col])

    if col < len(octopi[row])-1: 
        octopi[row][col+1] += 1
        if octopi[row][col+1] > 9: 
            q.append([row,col+1])

    if col > 0: 
        octopi[row][col-1] += 1
        if octopi[row][col-1] > 9: 
            q.append([row,col-1])

    if row > 0 and col > 0: 
        octopi[row-1][col-1] += 1
        if octopi[row-1][col-1] >9: 
            q.append([row-1, col-1])

    if row < len(octopi)-1 and col < len(octopi[row])-1:
        octopi[row+1][col+1] += 1
        if octopi[row+1][col+1] > 9: 
            q.append([row+1, col+1])

    if row < len(octopi)-1 and col > 0:
        octopi[row+1][col-1] += 1
        if octopi[row+1][col-1] > 9: 
            q.append([row+1, col-1])

    if row > 0 and col < len(octopi[row])-1:
        octopi[row-1][col+1] += 1
        if octopi[row-1][col+1] > 9: 
            q.append([row-1, col+1])

i = 0
while True:
    i += 1
    flashed = [[False for p in range(len(octopi[q]))] for q in range(len(octopi))]
    
    # Increase all octopi by 1
    for j in range(len(octopi)):
        for k in range(len(octopi[j])):
            octopi[j][k] += 1

    # Check for flashes
    for j in range(len(octopi)):
        for k in range(len(octopi[j])):
            flashed_q = []
            if octopi[j][k] > 9 and not flashed[j][k]:  
                flash(j, k, octopi, flashed, flashed_q)
             
            while len(flashed_q) > 0:

                curr = flashed_q.pop()
                row = curr[0]
                col = curr[1]
                if not flashed[row][col]:
                    flash(row, col, octopi, flashed, flashed_q)

    # Set all flashed octopi back to zero 
    allFlashed = True
    for j in range(len(flashed)):
        for k in range(len(flashed[j])):
            if flashed[j][k]:
                octopi[j][k] = 0 
            else:
                allFlashed = False
    if allFlashed: 
        print(i)
        break
    
#print(flashes)