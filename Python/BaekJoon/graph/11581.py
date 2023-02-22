# 11581번 구호물자
# https://www.acmicpc.net/problem/11581
import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())
if N==1:
    print('NO CYCLE')
    exit()
graph = [[] for _ in range(N)]
visit = [0]*(N+1)
for n in range(1, N):
    i = read()
    graph[n] = list(map(int, read().split()))

que = deque([1])
visit[1] = 0
while que:
    p = que.pop()
    for g in graph[p]:
        if g != N:
            if visit[g]==p:
                print('CYCLE')
                exit()
            que.append(g)
        visit[g] = p
print('NO CYCLE')