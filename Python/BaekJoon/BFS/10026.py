# 10026번 적록색약
# https://www.acmicpc.net/problem/10026
import sys
from collections import deque
read = sys.stdin.readline

def BFS(i, j):
    que.append((i, j))
    while que:
        x, y = que.popleft()
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and not visit[nx][ny] and pict[x][y]==pict[nx][ny]:
                que.append((nx,ny))
                visit[nx][ny] = 1

N = int(input())
que = deque()
pict = [list(read().strip()) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = [0,0]

# 적록색약 X
for row in range(len(pict)):
    for col in range(len(pict[0])):
        if not visit[row][col]:
            ans[0] += 1
            BFS(row,col)

for row in range(N):
    for col in range(N):
        if pict[row][col] == 'G':
            pict[row][col] = 'R'


visit = [[0 for _ in range(N)] for _ in range(N)]

for row in range(N):
    for col in range(N):
        if not visit[row][col]:
            ans[1] += 1
            BFS(row,col)
print(*ans)