from collections import deque

while True:
    sentence = input()
    if sentence == '.':
        exit()
    dec = deque()
    for i in sentence:
        if i == "[" or i == "(":
            dec.append(i)
        elif i == "]":
            if len(dec) == 0 or dec[-1] != "[":
                dec.append(-1)
                break
            else:
                dec.pop()
        elif i == ")":
            if len(dec) == 0 or dec[-1] != "(":
                dec.append(-1)
                break
            else:
                dec.pop()
    if len(dec) == 0:
        print("yes")
    else:
        print("no")