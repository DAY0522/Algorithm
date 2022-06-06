# 7576 토마토
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def is_ripen(g): # 그래프 내의 토마토가 모두 익었는지 확인. 다 익었으면 True, 아니면 False
    result = True
    for g in graph: # 처음부터 다 익은 경우
        if g.count(0) != 0:  # 0이 하나라도 있으면 break
            result = False
            break
    return result

def tomato():
    que = deque()
    day = -1
    for row in range(h):
        for col in range(w):
            if graph[row][col] == 1: # 초기 토마토의 위치
                que.append((row, col)) # 초기 토마토 (행, 열) 위치 삽입
    while que:
        day += 1
        s = len(que)
        for _ in range(s):
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx>=0 and nx<w and ny>=0 and ny<h and graph[ny][nx]==0:
                    graph[ny][nx]=1
                    que.append((ny, nx))
    if is_ripen(graph): print(day)
    else: print(-1)

if __name__ == '__main__':
    w, h = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(h) ]

    if is_ripen(graph): # 다 익은 경우
        print(0)
        exit()

    tomato()