import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    print(' '.join(map(str, result)))

topology_sort()