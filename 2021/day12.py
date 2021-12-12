inp = open('input.txt').read().split('\n')

caves_graph = {}

# Build graph 
for line in inp:
    curr = line.split('-')
    caveA = curr[0]
    caveB = curr[1]

    if caveA in caves_graph:
        caves_graph[caveA].append(caveB)
    else:
        caves_graph[caveA] = [caveB]

    if caveB in caves_graph: 
        caves_graph[caveB].append(caveA)
    else:
        caves_graph[caveB] = [caveA]

# Util function to check if any caves have been used twice yet
def findCaveUsedTwice(used):
    for cave in used:
        if used[cave] >= 2:
            return cave

    return None 

pathcount = 0 

# DFS
def find_path(currCave, currPath, usedSmalls, caves):
    global pathcount
   
    if currCave == 'end':
        pathcount += 1
    
    else:
        for adj in caves[currCave]:
            if adj != 'start':
                currPath.append(adj)
                if adj.lower() == adj:

                    # Check if a lowercase is valid to add to the path 
                    if adj in usedSmalls:
                        usedCount = usedSmalls[adj]

                        if usedCount >= 1: 
                            twoCave = findCaveUsedTwice(usedSmalls)
                            if twoCave is None:
                                usedSmalls[adj] += 1
                            else:
                                currPath.pop()
                                continue
                        else:
                            usedSmalls[adj] += 1
                    else:
                        usedSmalls[adj] = 1

                    # Part 1
                    # # If you've already used this small cave, it's not a valid path
                    # if adj in usedSmalls and usedSmalls[adj] > 0:
                    #     currPath.pop()
                    #     continue

                    # else:

                    #     if adj in usedSmalls:
                    #         usedSmalls[adj] += 1
                    #     else:
                    #         usedSmalls[adj] = 1
                        
                
                find_path(adj, currPath, usedSmalls, caves)
                removed = currPath.pop()
                if removed.lower() == removed:
                    usedSmalls[removed] -= 1

find_path('start', [], {}, caves_graph)
print(pathcount)