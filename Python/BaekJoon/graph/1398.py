# 1389번 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

ans = [0, float('inf')] # 유저 번호, 최솟값
for i in range(1, N+1):
    que = deque([i])
    visited = [False] * (N+1)
    visited[i] = True
    res = 0
    cnt = 0
    while que:
        len_q = len(que)
        cnt += 1
        for _ in range(len_q):
            p = que.popleft()
            for g in graph[p]:
                if not visited[g]:
                    res += cnt
                    visited[g] = True
                    que.append(g)
    if res < ans[1]:
        ans[1] = res
        ans[0] = i
print(ans[0])