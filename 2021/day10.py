inp = open('input.txt').read().split('\n')

starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']
scores = []
for line in inp: 
    score = 0
    s = []
    valid = True
    for chr in line: 
    
        if chr in starts:
            s.append(chr)
        elif chr in ends:
            if len(s) > 0: 
                top = s.pop()
                if (top == '(' and chr != ')') or (top == '{' and chr != '}') or (top == '[' and chr != ']') or (top == '<' and chr != '>'):
                    valid = False

                    # part 1
                    # if chr == ')':
                    #     score += 3
                    # elif chr == ']':
                    #     score += 57
                    # elif chr == '}':
                    #     score += 1197
                    # elif chr == '>':
                    #     score += 25137 
        if not valid: 
            break 
    
    # Handle incomplete lines
    if valid and len(s) > 0: 

        while len(s) > 0:
            top = s.pop()
            score *= 5

            if top == '(':
                score += 1
            elif top == '[':
                score += 2
            elif top == '{':
                score += 3
            elif top == '<':
                score += 4
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])