# 7569번 토마토
# https://www.acmicpc.net/problem/7569

# 여기선 visited가 굳이 필요 없다.
# 그냥 안 익어 있던 것을 익도록 바꿔주면 되니까!
# 즉 0>1로 변경하면 됨

import sys
from collections import deque
read = sys.stdin.readline

M, N, H = map(int, read().split())
box = list([list(map(int, read().split())) for _ in range(N)] for _ in range(H))
que = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토 위치 저장
for height in range(H):
    for row in range(N):
        for col in range(M):
            if box[height][row][col]==1:
                que.append((height,row,col))

ans = 0
while que:
    ans += 1
    s = len(que)
    for _ in range(s):
        z, x, y = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                que.append((nz, nx, ny))
                box[nz][nx][ny] = 1 # 익도록 변경

for height in range(H):
    for row in range(N):
        for col in range(M):
            if not box[height][row][col]: # 안 익은 게 있는 경우
                print(-1)
                exit()
print(ans-1)