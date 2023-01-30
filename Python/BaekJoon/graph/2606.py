# 2606번 바이러스
# https://www.acmicpc.net/problem/2606

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

que = deque([1])
visited[1] = True

cnt = 0
while que: # DFS로 풀이
    p = que.pop()
    for node in graph[p]:
        if not visited[node]:
            cnt += 1
            que.append(node)
            visited[node] = True
print(cnt)