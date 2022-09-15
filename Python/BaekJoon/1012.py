# 1012번 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
read = sys.stdin.readline

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, read().split()) # 열, 행, 개수
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    pos = deque()
    que = deque()
    for _ in range(K): # 배추 위치 저장
        y, x = map(int, read().split())
        cabbage[x][y] = 1
        pos.append((x, y))
    visit = [[0 for _ in range(M)] for _ in range(N)]


    ans = 0
    for i in range(len(pos)):
        if not visit[pos[i][0]][pos[i][1]]:
            que.append(pos[i])
            ans += 1
        while que:
            q_x, q_y = que.pop()
            visit[q_x][q_y] = 1
            for i in range(4):
                x = q_x + dx[i]
                y = q_y + dy[i]
                if x>=0 and x<N and y>=0 and y<M and not visit[x][y] and cabbage[x][y]:
                    que.append((x,y))
                    visit[x][y] = 1
    print(ans)