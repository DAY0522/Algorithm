import sys
from collections import deque

read = sys.stdin.readline

N = int(read().strip())
graph = [[0] * N for _ in range(N)]
for _ in range(int(read().strip())):
    x, y = map(int, read().split())
    graph[x - 1][y - 1] = 1  # 사과 체크

visit = [[False] * N for _ in range(N)]  # 현재 위치에 뱀이 있는지?
visit[0][0] = True

T = int(read().strip())
turn = []
for _ in range(T):  # turn 시간 등록
    t, d = read().split()
    turn.append((int(t), d))

# 좌 0 상 1 우 2 하 3
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

dir = 2  # 현재 방향
time = 0  # 현재 시간
cur = 0  # turn의 인덱스
que = deque([[0, 0]])
while True:
    time += 1  # 시간 증가

    # 몸길이를 늘려 머리를 다음칸에 위치
    x, y = que[0]
    x += dx[dir]
    y += dy[dir]
    if x < 0 or x >= N or y < 0 or y >= N or visit[x][y]:  # 이동하려는 자리에 뱀이 있거나, 벽에 닿은 경우
        break
    else:  # 뱀이 없는 경우
        que.appendleft([x, y])
        visit[x][y] = True  # 새롭게 이동한 자리에 방문 표시
        if graph[x][y] == 1:  # 사과가 있으면
            graph[x][y] = 0  # 사과 없애기
        else:  # 사과가 없으면
            r, c = que.pop()  # 끝의 위치 없애기
            visit[r][c] = False  # 비운 칸 미방문 표시

    # turn이 입력된 경우 해당 초가 끝나고 방향 변경
    if cur < T and time == turn[cur][0]:
        if turn[cur][1] == 'D':  # 오른쪽 90도
            dir = (dir + 1) % 4
        else:  # 왼쪽 90도
            dir = (dir - 1) % 4
        cur += 1

print(time)