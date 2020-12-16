import copy

puzzleInput = open('day16input.txt').read().strip().split('\n')

fields = {}

# Get fields and ranges
for line in puzzleInput: 

    if 'your ticket:' in line:
        break

    field = line[:line.find(':')]

    rangeOne = line[line.find(':') + 2 : line.find(' or ')]
    rangeTwo = line[line.find(' or ') + len(' or '):]

    if field != '':
        fields[field] = [rangeOne, rangeTwo]


# Loop through other ticket vals to find which ones contain any invalid values
invalidVals = 0
validTickets = []
for ticket in puzzleInput[puzzleInput.index('nearby tickets:') + 1 :]:

    ticketVals = ticket.split(',')
    validTicket = True

    # For each value, check against all ranges in fields
    for val in ticketVals: 
        allInvalid = True

        for field in fields:
            if allInvalid is False:
                break

            for fieldRange in fields[field]: 
                val = int(val)

                lowRange = int(fieldRange[:fieldRange.find('-')])
                highRange = int(fieldRange[fieldRange.find('-') + 1 :])

                if val >= lowRange and val <= highRange:
                    allInvalid = False
                    break
        
        if allInvalid is True:
            invalidVals = invalidVals + val
            validTicket = False
    
    # If the ticket did not have any invalid fields, add it to the
    # list of valid tickets to check for part 2
    if validTicket is True:
        validTickets.append(ticket)


# Part 1 answer
# print(invalidVals)

# Loop through each index in the order of ticket vals
# to determine which field it belongs to 
totalPotentialFields = list(fields.keys())
fieldChoices = {}

for i in range(len(ticketVals)): 
    currPotentialFields = copy.deepcopy(totalPotentialFields)
    
    for ticket in validTickets:
        
        currVal = int(ticket.split(',')[i])

        # Check against all potential fields
        for field in currPotentialFields:
            fieldRangeOne = fields[field][0]
            fieldRangeTwo = fields[field][1]

            lowRangeOne = int(fieldRangeOne[:fieldRangeOne.find('-')])
            highRangeOne = int(fieldRangeOne[fieldRangeOne.find('-') + 1 :])

            lowRangeTwo = int(fieldRangeTwo[:fieldRangeTwo.find('-')])
            highRangeTwo = int(fieldRangeTwo[fieldRangeTwo.find('-') + 1 :])

            if (currVal < lowRangeOne or currVal > highRangeOne) and (currVal < lowRangeTwo or currVal > highRangeTwo): 
                currPotentialFields.remove(field)
                break

    fieldChoices[i] = currPotentialFields


# Given the potential fields for each index, start with the 
# ones that can only be one field and build up to determine
# the final field for each 
finalFields = {}
for currLength in range(1, 21):
    for pos in fieldChoices:

        if len(fieldChoices[pos]) == currLength:
            
            for potentialField in fieldChoices[pos]:
                if potentialField in totalPotentialFields:
                    chosenField = potentialField

            totalPotentialFields.remove(chosenField)
            finalFields[chosenField] = pos



# Get your ticket
yourTicketVals = puzzleInput[puzzleInput.index('your ticket:') + 1].split(',')

# Multiply together all of your ticket vals that
# contain departure in their field names
result = 1
for field in finalFields:
    if 'departure' in field:
        pos = int(finalFields[field])
        yourVal = int(yourTicketVals[pos])
        result = result * yourVal

# Part 2 answer
print(result)


