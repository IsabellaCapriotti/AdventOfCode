puzzleInput = open('day19sample.txt').read().strip().split('\n')

origRules = {}
# Read all original rules into dictionary
for line in puzzleInput: 
    if ':' not in line:
        break

    ruleNum = int(line[:line.find(':')])
    origRules[ruleNum] = []

    ruleSet = line[line.find(':') + 1:].split('|')
    
    for rule in ruleSet:
        origRules[ruleNum].append(rule.strip().split(' '))

print(origRules)
# Function to get the root string expected by the rule 
def getRootRules(origRule):
    options = []
    for ruleOption in origRules[origRule]:
        currOption = []
        for ruleSpec in ruleOption:

            if '"' in ruleSpec:
                currOption.append(ruleSpec[1])   

            else:
                currOption.append(getRootRules(int(ruleSpec)))

        options.append(currOption)

    return options


for item in origRules:
    print(getRootRules(item))