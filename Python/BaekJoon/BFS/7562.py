# 7562 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque

read = sys.stdin.readline

for _ in range(int(read().strip())):
    N = int(read().strip())
    board = [[0 for _ in range(N)] for _ in range(N)]
    start = tuple(map(int, read().split()))
    end = tuple(map(int, read().split()))

    dx = [-1, -2, -1, -2, 1, 2, 1, 2]
    dy = [-2, -1, 2, 1, -2, -1, 2, 1]

    cnt = 0
    result = False
    que = deque()
    que.append(start)
    board[start[0]][start[1]] = 1

    if start == end:
        print(0)
        continue

    while que:
        size = len(que)
        cnt += 1
        for _ in range(size):
            x, y = que.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx == end[0] and ny == end[1]:
                    result = True
                if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                    que.append((nx, ny))
                    board[nx][ny] = 1
        if result:
            print(cnt)
            break