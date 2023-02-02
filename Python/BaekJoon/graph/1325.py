# 1325번 효율적인 해킹
# https://www.acmicpc.net/problem/1325
import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, read().split())
    graph[v].append(u)

result =[0]*(N+1)
for n in range(1, N+1):
    visit = [False] * (N+1)
    que = deque([n])
    visit[n] = True
    cnt = 0
    while que:
        p = que.popleft()
        for g in graph[p]:
            if not visit[g]:
                visit[g] = True
                que.append(g)
                cnt += 1
    result[n] = cnt

m = max(result)
for i in range(1, N+1):
    if result[i]==m:
        print(i, end=' ')