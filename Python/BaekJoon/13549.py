# 13549번 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
from collections import deque

N, K = map(int, input().split())
visited = [0] * 200000

if K <= N:
    print(N - K)
    exit()

que = deque()
que.append(N)
visited[N] = 1

while not visited[K]:
    x = que.popleft()
    if (2 * x < K or 2 * x - K < K - x) and not visited[2 * x]:
        que.appendleft(2 * x)
        visited[2 * x] = visited[x]

    if x > 0 and not visited[x - 1]:
        que.append(x - 1)
        visited[x - 1] = visited[x] + 1

    if x < K and not visited[x + 1]:
        que.append(x + 1)
        visited[x + 1] = visited[x] + 1

print(visited[K] - 1)