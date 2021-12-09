crabs = [int(i) for i in open('input.txt').read().split(',')]

possible_vals = set(crabs)

best_diff = -1 

for val in range(min(crabs), max(crabs)): 
    
    curr_increment = [1 for i in range(len(crabs))]
    fuel = 0 

    for i in range(len(crabs)):
        diff = abs(val - crabs[i])
        # part 1
        #fuel += diff
        fuel += (diff * (diff + 1)) / 2
        
    if best_diff == -1 or fuel < best_diff:
        best_diff = fuel

print(best_diff)