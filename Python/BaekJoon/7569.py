# 7569번 토마토
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
read = sys.stdin.readline

M, N, H = map(int, read().split())
box = list([list(map(int, read().split())) for _ in range(N)] for _ in range(H))
visited = list([[0 for _ in range(M)] for _ in range(N)] for _ in range(H))
que = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토 위치 저장
for height in range(H):
    for row in range(N):
        for col in range(M):
            if box[height][row][col]==1:
                visited[height][row][col] = 1
                que.append((height,row,col))

while que:
    z, x, y = que.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and not visited[nz][nx][ny] and box[nz][nx][
            ny] == 0:
            que.append((nz, nx, ny))
            visited[nz][nx][ny] = visited[z][x][y] + 1

days = 0
for height in range(H):
    for row in range(N):
        for col in range(M):
            days = max(days, visited[height][row][col])
            if not visited[height][row][col] and box[height][row][col]==0:
                print(-1)
                exit()
print(days-1)