# 2606 바이러스
import sys
from collections import deque
read = sys.stdin.readline

def BFS():
    que = deque([1]) # create queue with start node
    visit[1] = True

    while que: # queue is not empty
        n = que.popleft()
        for i in graph[n]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

if __name__ == '__main__':
    n = int(read())  # 컴퓨터 수(node)
    e = int(read())  # 컴퓨터쌍 수(edge)

    graph = [[] for _ in range(n+1)]  # create graph
    for _ in range(e):  # graph initailization
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [False for _ in range(n+1)] # create visit list
    BFS()
    print(visit.count(1)-1)