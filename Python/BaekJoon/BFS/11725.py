# 11725번 트리의 부모 찾기
import sys
from collections import deque
read = sys.stdin.readline

def BFS():
    parent = [ 0 for _ in range(N+1)]
    que = deque([1])
    visited[1] = 1
    while que:
        node = que.popleft()
        for n in graph[node]:
            if visited[n] == 0: # 방문한 적이 없으면
                que.append(n)
                visited[n] = 1
                parent[n] = node
    for i in range(2, N+1):
        print(parent[i])

if __name__ == '__main__':
    N = int(read())
    visited = [ 0 for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)
    BFS()