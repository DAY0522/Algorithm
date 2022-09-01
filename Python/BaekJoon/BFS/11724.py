# 11724 연결 요소의 개수
import sys
from collections import deque
read = sys.stdin.readline

def BFS(start):
    que = deque([start])
    visited[start] = 1

    while que: # que is not empty
        node = que.popleft()
        for n in graph[node]:
            if not visited[n]:
                que.append(n)
                visited[n] = 1


if __name__ == '__main__':
    N, E = map(int, read().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(E):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(N + 1)]
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            BFS(i)
    print(cnt)
