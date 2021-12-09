inp = open('input.txt').read().split('\n')
heatmap = []
for line in inp:
    heatmap.append([int(i) for i in line])

risk = 0
basins = []
for i in range(len(heatmap)):
    for j in range(len(heatmap[i])): 

        lowPoint = True 
        # l
        if j > 0 and heatmap[i][j-1] <= heatmap[i][j]: 
            lowPoint = False

        # r
        if j < len(heatmap[i])-1 and heatmap[i][j+1] <= heatmap[i][j]:
            lowPoint = False
          

        # u 
        if i > 0 and heatmap[i-1][j] <= heatmap[i][j]:
            lowPoint = False
   

        #d
        if i < len(heatmap)-1 and heatmap[i+1][j] <= heatmap[i][j]: 
            lowPoint = False


        if lowPoint: 
            basinSize = 0

            # find all non-9s adjacent to the low point, plus all non-9s adjacent to those.. and so on 
            processed = {}
            q = [[i,j]]

            while len(q) > 0: 
                currPoint = q.pop()

                if str(currPoint) not in processed: 
                    basinSize += 1
                    processed[str(currPoint)] = True
                    row = currPoint[0]
                    col = currPoint[1]

                    # l
                    if col > 0 and heatmap[row][col-1] != 9:
                        q.append([row, col-1])

                    # r
                    if col < len(heatmap[row])-1 and heatmap[row][col+1] != 9:
                        q.append([row, col+1])
                    

                    # u 
                    if row > 0 and heatmap[row-1][col] != 9:
                        q.append([row-1, col])
            

                    #d
                    if row < len(heatmap)-1 and heatmap[row+1][col] != 9: 
                        q.append([row+1, col])


            basins.append(basinSize)

basins.sort(reverse=True)
prod = 1
for basin in basins[:3]:
    prod *= basin

print(prod)
