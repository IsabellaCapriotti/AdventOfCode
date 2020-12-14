file = open("day7input.txt")
input = file.read().strip().split('\n')

# Get dictionary with bag name as key and array of other bags as value
bagVals = dict()

# Part 1
for line in input: 
    # Name of bags
    bagsPos = line.find("bags")
    bagName = line[:bagsPos - 1]

    bagVals[bagName] = []

    # Other bags that can fit
    commaSections = line[bagsPos + 13:].split(',')

    for section in commaSections:
        numberPos = -1 

        for i, character in enumerate(section):
            if character.isdigit():
                numberPos = i
                break
 
        if numberPos == -1:
            bagVals[bagName].append("none")
            break

        bagType = section[numberPos:section.find("bag") - 1]
        bagVals[bagName].append(bagType)


shinyGoldCount = 0

def checkForGold(nameOfBag, memo={}):

    if 'shiny gold' in bagVals[nameOfBag]:
        memo[nameOfBag] = True
        return True
    elif 'none' in bagVals[nameOfBag]:
        memo[nameOfBag] = False
        return False

    elif nameOfBag in memo:
        return memo[nameOfBag]

    else:
        for bag in bagVals[nameOfBag]:
            if checkForGold(bag, memo) is True:
                memo[bag] = True
                return True
        memo[bag] = False
        return False


# Search for shiny gold bags
for bagName in bagVals.keys():
    if checkForGold(bagName) is True:
        shinyGoldCount = shinyGoldCount + 1
 
print(shinyGoldCount)


# Part 2
# Start with original shiny gold bag
def findBags(currentBag, parentNum, memo = {}):

    if 'none' in bagVals[currentBag]:
        return 0 

    else:
        childSum = 0 

        for bag in bagVals[currentBag]:
            # Get number
            num = bag[0]
            name = bag[bag.find(num) + 2:]
            num = int(num)

            if bag in memo:
                childSum = childSum + num + memo[bag]
            else:
                memo[bag] = findBags(name, num, memo)
                childSum = childSum + num + memo[bag]
        
        return parentNum * childSum


print(findBags('shiny gold', 1, {}))

        
