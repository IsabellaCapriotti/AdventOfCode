# Comb sort
def getNextGap(currGap):
    currGap = (currGap *10)//13
    if(currGap < 1):
        return 1
    return currGap

def combSort(listToSort):
    length = len(listToSort)
    
    swapped = True

    gap = length

    while gap > 1 or swapped == True:
        
        gap = getNextGap(gap)

        swapped = False

        for i in range(0, length - gap):

            if listToSort[i] >= listToSort[i + gap]:
                temp = listToSort[i]
                listToSort[i] = listToSort[i+gap]
                listToSort[i+gap] = temp
                swapped = True
            

# Find element
def findSumElements(list, desiredSum):
    for i in range(0, len(list)): 
        for j in range(i + 1, len(list)): 
            for k in range(j + 1, len(list)):
                if list[i] + list[j] + list[k] == desiredSum: 
                    return (list[i], list[j], list[k])
            

    return 0 


# Get input
input = list()
inputFile = open("day1input.txt", "r")

fileString = inputFile.read() 
input = fileString.split('\n')

for i, string in enumerate(input):
    input[i] = (int)(string)
    
# Sort input
combSort(input)

print(findSumElements(input, 2020))












