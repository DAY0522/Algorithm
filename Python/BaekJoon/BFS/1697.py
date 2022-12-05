# 1697번 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque
N, K = map(int, input().split())
visit = [0 for _ in range(200000)]
que = deque()
que.append(N)

visit[que[0]] = 1
while que:
    que_size = len(que)
    for _ in range(que_size):
        p = que.popleft()

        if p-1 >= 0 and not visit[p-1]:
            visit[p-1] = visit[p] + 1
            que.append(p-1)
        if N < K and p+1 <= K and not visit[p+1]:
            visit[p+1] = visit[p] + 1
            que.append(p+1)

        if p*2 < 200000 and not visit[p*2]:
            visit[p*2] = visit[p] + 1
            que.append(p*2)

    if visit[K]:
        print(visit[K]-1)
        exit()