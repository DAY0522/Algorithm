# 2170번 선 긋기
# https://www.acmicpc.net/problem/2170
import sys
read = sys.stdin.readline

N = int(read().strip())
pos = [list(map(int, read().split())) for _ in range(N)]
pos.sort(key = lambda x:(x[0], x[1]))
ans = 0
prev_y = -1000000000
for x, y in pos:
    if y <= prev_y:
        continue
    elif x < prev_y:
        ans += abs(y - prev_y)
    else:
        ans += abs(y - x)
    prev_y = y
print(ans)