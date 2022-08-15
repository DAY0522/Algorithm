# 5567번 결혼식
# https://www.acmicpc.net/problem/5567

# 친구의 친구까지만 초대
# 상근이의 학번은 1

import sys
from collections import deque
read = sys.stdin.readline

n = int(read().strip())
m = int(read().strip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS로 풀이
que = deque(graph[1])
visited[1] = True
for g in graph[1]:
    visited[g] = True
cnt = len(graph[1])

for i in range(len(graph[1])):
    p = que.popleft()
    for g in graph[p]:
        if not visited[g]:
            cnt += 1
            que.append(g)
            visited[g] = True
print(cnt)