# 5427번 불
# https://www.acmicpc.net/submit/5427/52701604

'''
56번 라인을 다음과 같이 썼다가 시간 초과가 났다.
if t == '@' and maze[nx][ny] == '.' and not S_visit[nx][ny] and (time < F_visit[nx][ny] or F_visit[nx][ny] == 0):

혹시나 이전에 도달한 불의 시간이 상근이가 도달한 시간보다 적은 경우를 생각해 다음과 같은 조건을 넣어준 것인데, 이런 경우는 발생하지 않는다.
time < F_visit[nx][ny] -> 어차피 같은 시간에 한 칸씩 동일하게 퍼지기 때문에 이미 불이 퍼진 곳은 못 가는 곳이기 때문이다.
해당 조건문을 확인하는 과정에서 시간 초과가 발생한 것으로 보인다.
(time < F_visit[nx][ny] or F_visit[nx][ny] == 0)
'''


import sys
from collections import deque
read = sys.stdin.readline

for _ in range(int(read().strip())):
    w, h = map(int, read().split())
    maze = [read().strip() for _ in range(h)]
    F_visit = [[0 for _ in range(w)] for _ in range(h)]
    S_visit = [[0 for _ in range(w)] for _ in range(h)]
    que = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = 1
    ans = 0

    for row in range(h):
        for col in range(w):
            c = maze[row][col]
            if c == '@':  # 상근이거나 불이면
                S_pos = (row, col, c)
                S_visit[row][col] = time
                if row == 0 or col == 0 or row == h-1 or col == w-1:
                    ans = time
            elif c == '*':
                que.append((row, col, c))
                F_visit[row][col] = time
    if ans:
        print(time)
        continue

    que.append(S_pos)

    while que:
        size = len(que)
        time += 1
        for _ in range(size):
            x, y, t = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if t == '@' and maze[nx][ny] == '.' and not S_visit[nx][ny] and not F_visit[nx][ny]:
                        que.append((nx, ny, t))
                        S_visit[nx][ny] = time
                        if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                            ans = time

                    elif t == '*' and maze[nx][ny] != '#' and not F_visit[nx][ny] and not S_visit[nx][ny]:
                        que.append((nx, ny, t))
                        F_visit[nx][ny] = time
        if ans:
            print(ans)
            break
    if not ans:
        print("IMPOSSIBLE")