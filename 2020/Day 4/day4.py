file = open("day4input.txt")
input = file.read().split('\n\n')
count = 0 

neededKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validHex = ['a', 'b', 'c', 'd', 'e', 'f']
validCount = 0 

for line in input:

    foundKeys = list(neededKeys)
    colonPos = line.find(':')
    nextSpacePos = 0
    nextEndlPos = 0
    valid = True

    while (nextSpacePos != -1 or nextEndlPos != -1) and valid is True:
      
        # Get key, remove from running list of needed keys
        # if appropriate
        key = line[colonPos - 3:colonPos]    
        if key in neededKeys: 
            foundKeys.remove(key)

        # Get value after key
        nextSpacePos = line.find(' ')
        nextEndlPos = line.find('\n')

        if nextSpacePos != -1 and (nextEndlPos == -1 or nextSpacePos < nextEndlPos):
            value = line[colonPos + 1 : nextSpacePos].strip()
            line = line[nextSpacePos + 1:]

        elif nextSpacePos == -1 and nextEndlPos == -1:
            value = line[colonPos + 1:]

        else:
            value = line[colonPos + 1: nextEndlPos].strip()
            line = line[nextEndlPos + 1:]
       
        
        # Validity checks
        if key == 'byr':

            if len(value) != 4:
                valid = False
            else:
                if (int)(value) < 1920 or (int)(value) > 2002:
                    valid = False

        elif key == 'iyr':

            if len(value) != 4:
                valid = False
            else:
                if (int)(value) < 2010 or (int)(value) > 2020:
                    valid = False

        elif key == 'eyr':

            if len(value) != 4:
                valid = False
            else:
                if (int)(value) < 2020 or (int)(value) > 2030:
                    valid = False

        elif key == 'hgt':

            if(len(value) < 2):
                valid = False

            elif value[len(value) - 1] == 'm' and value[len(value) - 2] == 'c':
                measurement = value[0:value.find('c')]
                if (int)(measurement) < 150 or (int)(measurement) > 193:
                    valid = False

            elif value[len(value) - 1] == 'n' and value[len(value) - 2] == 'i':
                measurement = value[0:value.find('i')]
                if (int)(measurement) < 59 or (int)(measurement) > 76:
                    valid = False

            else:
                valid = False

        elif key == 'hcl': 
            if len(value) == 0 or value[0] != '#' or len(value) != 7:
                valid = False
            else: 
                for letter in value[1:]:
                    if not letter.isalnum():
                        valid = False
                        break
                    elif letter.isalpha() and letter not in validHex:
                        valid = False
                        break


        elif key == 'ecl': 
            if value not in validEyeColors:
                valid = False


        elif key == 'pid': 
            if(len(value) != 9):
                valid = False
            else:
                for letter in value: 
                    if not letter.isnumeric():
                        valid = False
        
        # Go to next key 
        colonPos = line.find(':')
       

    # If all needed keys were used, passport is valid  
    if len(foundKeys) == 0 and valid is True: 
        validCount = validCount + 1


print("Valid count:", validCount)