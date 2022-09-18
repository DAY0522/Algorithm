# 2573번 빙산
# https://www.acmicpc.net/source/52865878

import sys
from collections import deque

read = sys.stdin.readline

R, C = map(int, read().split())
iceberg = [list(map(int, read().split())) for _ in range(R)]
ice = deque()  # 각 빙산의 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not visited[nx][ny] and iceberg[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = True


def remove_iceberg(i, j):
    iceberg[i][j] = max(0, iceberg[i][j] - remove[i][j])
    if iceberg[i][j] <= 0:
        ice.remove((i, j))


for r in range(1, R - 1):
    for c in range(1, C - 1):
        if iceberg[r][c]:
            ice.append((r, c))  # 빙산의 위치 저장

ans = 0
cnt = 1  # 현재 빙산 덩어리 개수
while True:
    remove = [[0 for _ in range(C)] for _ in range(R)]
    size = len(ice)
    for i in range(size):
        x, y = ice[i]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if iceberg[nx][ny] <= 0:  # 빙산이 아닌 경우 count
                remove[x][y] += 1

    ans += 1
    for x, y in list(ice)[:]:  # 빙산이 녹은 경우 제거
        remove_iceberg(x, y)

    cnt = 0
    visited = [[False for _ in range(C)] for _ in range(R)]
    for x, y in ice:
        if iceberg[x][y] and not visited[x][y]:
            cnt += 1
            bfs(x, y)

    if cnt >= 2:  # 두 덩어리 이상 분리 된 경우
        print(ans)
        exit()
    elif not cnt:  # 빙산이 아예 없어진 경우
        print(0)
        exit()