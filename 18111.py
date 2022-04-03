import sys, math
input = sys.stdin.readline

N, M, inven = map(int, input().split())
lands = []
for i in range(N):
    lands += list(map(int, input().split()))
lands = sorted(lands)[::-1]
top, bottom = math.floor((inven+sum(lands))/(N*M)), min(lands)

mintime = float('inf')
Maxheight = 0

# 최종적으로 inven >= 0이 보장
for height in range(bottom, top+1):
    t = 0
    for l in lands:
        if l > height:
            t += 2*(l - height)
        elif l < height:
            t += (height - l)
        if t > mintime:
            break
    if t <= mintime:
        mintime = t
        if height > Maxheight:
            Maxheight = height
print(mintime, Maxheight)