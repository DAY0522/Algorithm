# 11043번 경로 찾기
# https://www.acmicpc.net/problem/11403

import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    li = list(map(int, read().split()))
    for j in range(N):
        if li[j] == 1:
            graph[i].append(j+1)

result = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    que = deque([i])

    while que:
        p = que.pop()
        for g in graph[p]:
            if not result[i][g]:
                que.append(g)
                result[i][g] = 1

for i in range(1, N+1):
    print(*(result[i][1:N+1]))