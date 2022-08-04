# 2847번 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847
import sys
read = sys.stdin.readline

N = int(read().strip())
score = [int(read().strip()) for _ in range(N)]
res = 0
for i in range(N-1, 0, -1):
    if score[i]<=score[i-1]:
        sub = score[i]-1
        res += score[i-1]-sub
        score[i-1] = sub
print(res)