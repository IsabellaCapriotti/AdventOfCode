file = open('day9input.txt')
input = file.read().strip().split('\n')

# Part 1

def checkSums(nums, targetVal):
    for j in range(len(nums)): 
        for k in range(j+1, len(nums)):
            if nums[j] + nums[k] == targetVal:
                return True

    return False

for i in range(25, len(input)):

    sumVals = []

    # Get value needed to sum to
    targetVal = int(input[i])

    # Get possible sum values
    j = i - 1

    while(j >= i - 25):
        sumVals.append(int(input[j]))
        j = j - 1


    # Loop through sum values
    if(checkSums(sumVals, targetVal)):
        continue

    else:
        print(targetVal, 'failed')
        break
    

# Part 2    
finalTargetVal = targetVal


for i in range(len(input)): 

    # Start with current number 
    currNum = int(input[i])

    # Loop through every possible range of sums
    # within the array 
    # Maintain running sum, see if it equals target at the end
    # Break early if greater than target

    currRange = 2

    while(currRange <= len(input) - i): 

        runningSum = currNum
        rangeVals = []
        rangeVals.append(currNum)

        innerIndex = i + 1
        rangeCount = 0
        
        overSum = False
        while(rangeCount < currRange and overSum is False): 
            endNum = int(input[innerIndex])

            runningSum = runningSum + endNum
            rangeVals.append(endNum)

            if(runningSum > finalTargetVal):
                overSum = True

            innerIndex = innerIndex + 1
            rangeCount = rangeCount + 1

        if runningSum == finalTargetVal:
            print('Starting number', currNum)
            print(rangeVals)
            print(min(rangeVals))
            print(max(rangeVals))
            break

        currRange = currRange + 1

    