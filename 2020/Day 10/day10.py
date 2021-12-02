import copy

file = open('day10input.txt')
input = file.read().strip().split('\n')

for i, val in enumerate(input):
    input[i] = int(val)

input.sort()

# Part 1
unusedAdapters = copy.deepcopy(input)

differences = {
    1: 0,
    2: 0,
    3: 0
}

currAdapter = 0
i = 0

while(len(unusedAdapters) > 0): 

    for j in range(i, len(input)): 
        diff = input[j] - currAdapter
        
        if diff > 0 and diff <=3 and input[j] in unusedAdapters: 
            differences[diff] = differences[diff] + 1
            unusedAdapters.remove(input[j])
            currAdapter = input[j]
            break

    if i == len(input) - 1: 
        differences[3] = differences[3] + 1
        break

    i = i + 1


print(differences[1], differences[2], differences[3])



# Part 2

def getCombos(currAdapter, adapters, memo): 
    count = 0 

    if currAdapter == max(adapters):
        return 1
    
    elif currAdapter in memo:
        return memo[currAdapter]


    if currAdapter + 1 in adapters: 
        count = count + getCombos(currAdapter + 1, adapters, memo)
        memo[currAdapter] = count
    if currAdapter + 2 in adapters: 
        count = count + getCombos(currAdapter + 2, adapters, memo)
        memo[currAdapter] = count
    if currAdapter + 3 in adapters:
        count = count + getCombos(currAdapter + 3, adapters, memo)
        memo[currAdapter] = count


    return count


print(getCombos(0, input, {}))