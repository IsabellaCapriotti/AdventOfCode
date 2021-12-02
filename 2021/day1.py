depths = open('input.txt').read()
depths_list = depths.split('\n')
inc = 0 
currSum = -1
prevSum = -1

for i in range(0, len(depths_list)-2):
    currSum = int(depths_list[i]) + int(depths_list[i+1]) + int(depths_list[i+2])

    if prevSum != -1 and currSum > prevSum: 
        inc += 1
    prevSum = currSum 

print('Increasing: ', inc)