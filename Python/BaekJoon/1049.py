# 1049번 기타줄
# https://www.acmicpc.net/problem/1049
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
pack = []
cnt = []

cost = float('inf')
for _ in range(M):
    p, c = map(int, read().split())
    pack.append(p)
    cnt.append(c)

p = min(pack)
c = min(cnt)
print(min(p*(N//6)+min(p, c*(N%6)), c*N))
