lines = open('input.txt').read().split('\n')
covered = {}

for line in lines:
    coords = line.split('->')
    start = [int(i) for i in coords[0].strip().split(',')]
    end = [int(i) for i in coords[1].strip().split(',')]

    
    # get points covered
    # vertical
    if start[0] == end[0]:
        first_point = min(start[1], end[1])
        last_point = max(start[1], end[1])

        while first_point <= last_point:
            if str([start[0], first_point]) in covered:
                covered[str([start[0], first_point])] += 1
            else:
                covered[str([start[0], first_point])] = 1

            first_point += 1
    
    # horizontal
    elif start[1] == end[1]:
        first_point = min(start[0], end[0])
        last_point = max(start[0], end[0])

        while first_point <= last_point:
            if str([first_point, start[1]]) in covered:
                covered[str([first_point, start[1]])] += 1
            else:
                covered[str([first_point, start[1]])] = 1

            first_point += 1
    # diagonals
    else:
        x_inc = False
        y_inc = False

        if start[0] < end[0]:
            x_inc = True

        if start[1] < end[1]: 
            y_inc = True

        curr_x = start[0]
        curr_y = start[1]

        if x_inc and y_inc:
            while curr_x <= end[0] and curr_y <= end[1]:
                
                if str([curr_x, curr_y]) in covered:
                    covered[str([curr_x,curr_y])] += 1
                else:
                    covered[str([curr_x,curr_y])] = 1

                curr_x += 1
                curr_y += 1

        elif x_inc and not y_inc:
            while curr_x <= end[0] and curr_y >= end[1]:
               

                if str([curr_x, curr_y]) in covered:
                    covered[str([curr_x,curr_y])] += 1
                else:
                    covered[str([curr_x,curr_y])] = 1

                curr_x += 1
                curr_y -= 1

        elif (not x_inc) and y_inc:
           
            while curr_x >= end[0] and curr_y <= end[1]:
                
                if str([curr_x, curr_y]) in covered:
                    covered[str([curr_x,curr_y])] += 1
                else:
                    covered[str([curr_x,curr_y])] = 1

                curr_x -= 1
                curr_y += 1

        elif not x_inc and not y_inc:
            
            while curr_x >= end[0] and curr_y >= end[1]:
                
                if str([curr_x, curr_y]) in covered:
                    covered[str([curr_x,curr_y])] += 1
                else:
                    covered[str([curr_x,curr_y])] = 1

                curr_x -= 1
                curr_y -= 1


        

count = 0
for key in covered:
    if covered[key] >= 2:
        count += 1

print(count)

    


