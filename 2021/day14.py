import copy

inp = open('input.txt').read().split('\n')

template = inp[0]

mappings = {}

for rule in inp[2:]:
    curr = rule.split('->')
    mappings[curr[0].strip()] = curr[1].strip()

pairs = {}
chrcounts = {}

# initialize pairs and character counts
for i in range(len(template)):

    if i < len(template)-1: 
        currpair = template[i:i+2]
        if currpair in pairs:
            pairs[currpair] += 1
        else:
            pairs[currpair] = 1

    if template[i] in chrcounts:
        chrcounts[template[i]] += 1
    else: 
        chrcounts[template[i]] = 1


for i in range(40):
    newpairs = copy.deepcopy(pairs)

    for p in pairs: 
        if pairs[p] > 0 and p in mappings:
            match = mappings[p]
            created = [p[0] + match, match + p[1]]

            # add new pairs spawned from this
            for newpair in created:
                if newpair in newpairs:
                    newpairs[newpair] += pairs[p]
                else:
                    newpairs[newpair] = pairs[p]

            # add to character count
            if match in chrcounts:
                chrcounts[match] += pairs[p]
            else:
                chrcounts[match] = pairs[p]

            # subtract old pairs that no longer exist
            newpairs[p] -= pairs[p]

    pairs = copy.deepcopy(newpairs)


# count results
mostFreqCount = -1
leastFreqCount = -1

for c in chrcounts:
    if mostFreqCount == -1 or chrcounts[c] > mostFreqCount:
        mostFreqCount = chrcounts[c]
    if leastFreqCount == -1 or chrcounts[c] < leastFreqCount: 
        leastFreqCount = chrcounts[c]

print(mostFreqCount - leastFreqCount)

# First method that wasn't efficient enough to work for part 2 
# for i in range(40):

#     new = template
#     charsAdded = 0 

#     for j in range(len(template)):
#         currpair = template[j:j+2]
#         if currpair in mappings:
#             new = new[:j+1+charsAdded] + mappings[currpair] + new[j+1+charsAdded:]
#             charsAdded += 1
    
#     #print(new)
#     template = new

