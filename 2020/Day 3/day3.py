file = open("day3input.txt")
treeMap = file.read().split('\n')
treeChar = "#"


def findTrees(list, rowSlope, colSlope): 
    rowIndex = 0
    colIndex = 0

    treeCount = 0

    while rowIndex < len(treeMap):
        
        # Go right 3, down 1    
        colIndex = (colIndex + colSlope) % len(treeMap[rowIndex])

        rowIndex = rowIndex + rowSlope
        

        if rowIndex >= len(treeMap) - 1:
            break

        elif treeMap[rowIndex][colIndex] == treeChar:
            treeCount = treeCount + 1


    print('Tree Count:', treeCount)

findTrees(treeMap, 1, 1)
findTrees(treeMap, 1, 3)
findTrees(treeMap, 1, 5)
findTrees(treeMap, 1, 7)
findTrees(treeMap, 2, 1)