# 2206번 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
maze = [list(map(int, read().strip())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()
que.append((0, 0, 0))
visited[0][0][0] = 1

while que:
    x, y, z = que.popleft()
    if x==N-1 and y==M-1:
        print(visited[x][y][z])
        exit()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<M:
            if maze[nx][ny]==0 and visited[nx][ny][z]==0:
                que.append((nx,ny,z))
                visited[nx][ny][z] = visited[x][y][z] + 1
            elif maze[nx][ny]==1 and z==0:
                que.append((nx,ny,1))
                visited[nx][ny][1] = visited[x][y][0] + 1

print(-1)