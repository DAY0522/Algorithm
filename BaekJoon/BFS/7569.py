# 7576 토마토
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우 위 아래
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def is_ripen(g): # 그래프 내의 토마토가 모두 익었는지 확인. 다 익었으면 True, 아니면 False
    result = True
    for g in graph: # 처음부터 다 익은 경우
        for line in g:
            if line.count(0) != 0:  # 0이 하나라도 있으면 break
                result = False
                break
    return result

def tomato():
    que = deque()
    day = -1
    for height in range(h):
        for row in range(n):
            for col in range(m):
                if graph[height][row][col] == 1: # 초기 토마토의 위치
                    que.append((height, row, col)) # 초기 토마토 (행, 열) 위치 삽입
    while que:
        day += 1
        s = len(que)
        for _ in range(s):
            z, y, x = que.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx>=0 and nx<m and ny>=0 and ny<n and nz>=0 and nz<h and graph[nz][ny][nx]==0:
                    graph[nz][ny][nx]=1
                    que.append((nz, ny, nx))
    if is_ripen(graph): print(day)
    else: print(-1)

if __name__ == '__main__':
    m, n, h = map(int, read().split())
    graph = [[list(map(int, read().split())) for _ in range(n)] for _ in range(h)]

    if is_ripen(graph): # 다 익은 경우
        print(0)
        exit()

    tomato()