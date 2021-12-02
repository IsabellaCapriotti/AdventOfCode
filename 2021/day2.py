input = open('input.txt').read().split('\n')
depth = 0 
pos = 0 
aim = 0

for line in input: 
    sep = line.split(' ')

    direction = sep[0]
    amount = sep[1]

    if direction == 'forward':
        pos += int(amount)
        depth += int(amount) * aim
    elif direction == 'up': 
        aim -= int(amount)
    elif direction == 'down':
        aim += int(amount)

print(depth * pos)