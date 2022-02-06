s = input() # test case size

for i in range(int(s)):
    test = input()
    score = 0
    total = 0
    for t in test:
        score += 1
        if t == "X":
            score = 0
        total += score
    print(total)