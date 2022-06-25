# 1926번 그림
# https://www.acmicpc.net/problem/1926

import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, input().split())
picture = list(list(map(int, read().strip().split())) for _ in range(n))
visit = list([0 for _ in range(m)] for _ in range(n))
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열
q = deque()
ans = 0
max_size = 0

for col in range(m):
    for row in range(n):
        if not visit[row][col] and picture[row][col]: # 방문하지 않고, 색칠 됐을 때
            size = 1
            q.append((row, col))
            visit[row][col] = 1
            while q: # q가 빌 때까지 계속 진행
                p_x, p_y = q.popleft()
                for i in range(4):
                    x = p_x + dx[i]
                    y = p_y + dy[i]
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if picture[x][y] and not visit[x][y]: # 색칠 돼있고 방문 안 했을 시 q에 추가
                            size += 1
                            q.append((x,y))
                            visit[x][y] = 1
            max_size = max(max_size, size)
            ans += 1
print(ans)
print(max_size)