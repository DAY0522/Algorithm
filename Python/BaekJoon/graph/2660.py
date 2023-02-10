# 2660번 회장뽑기
# https://www.acmicpc.net/problem/2660
import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())
graph = [[] for _ in range(N+1)]

while True:
    u, v = map(int, read().split())
    if u==-1 and v==-1:
        break
    graph[u].append(v)
    graph[v].append(u)

result = [100] + [0] * (N)
for n in range(1, N+1):
    visited = [False] * (N + 1)
    que = deque([n])
    visited[n] = True
    cnt = -1
    while que:
        cnt += 1
        len_q = len(que)
        for _ in range(len_q):
            p = que.popleft()
            for g in graph[p]:
                if not visited[g]:
                    que.append(g)
                    visited[g] = True
    result[n] = cnt

m = min(result)
candi = []
for i in range(1, N+1):
    if result[i]==m:
        candi.append(i)
print(m, len(candi))
print(*candi)