fishies = {}

for fish in open('input.txt').read().split(','):
    if int(fish) in fishies:
        fishies[int(fish)] += 1
    else:
        fishies[int(fish)] = 1

new_fishies = {}

for i in range(256):
    for counter in fishies: 
        if counter == 0:
            if 6 in new_fishies:
                new_fishies[6] += fishies[counter]
            else:
                new_fishies[6] = fishies[counter]
            if 8 in new_fishies:
                new_fishies[8] += fishies[counter]
            else:
                new_fishies[8] = fishies[counter]
        else:
            if counter-1 in new_fishies: 
                new_fishies[counter-1] += fishies[counter]
            else:
                new_fishies[counter-1] = fishies[counter]
    fishies = new_fishies
    new_fishies = {}
print(sum(fishies.values()))


