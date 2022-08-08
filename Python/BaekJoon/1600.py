# 1600번 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600

import sys
from collections import deque

read = sys.stdin.readline

K = int(read().strip())  # 말 이동 횟수
C, R = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(R)]
visited = [[[0 for _ in range(K + 1)] for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0, -2, -2, -1, -1, 2, 2, 1, 1, ]
dy = [0, 0, -1, 1, -1, 1, -2, 2, -1, 1, -2, 2]

que = deque()
que.append((0, 0, 0))
visited[0][0][0] = 1

while que:
    x, y, z = que.popleft()

    if x == R - 1 and y == C - 1:
        print(visited[x][y][z] - 1)
        exit()
    for d in range(0, 4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 1 and not visited[nx][ny][z]:
            que.append((nx, ny, z))
            visited[nx][ny][z] = visited[x][y][z] + 1

    if z < K:
        for d in range(4, 12):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 1 and not visited[nx][ny][z + 1]:
                que.append((nx, ny, z + 1))
                visited[nx][ny][z + 1] = visited[x][y][z] + 1

print(-1)