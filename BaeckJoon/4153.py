import sys
input = sys.stdin.readline
while True:
    lines = list(map(int, input().split()))
    hypo = max(lines)
    lines.remove(hypo)
    if sum(lines) == 0:
        exit()
    if lines[0]**2 + lines[1]**2 == hypo**2:
        print("right")
    else:
        print("wrong")