# 1926번 그림
import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
pict = list() # 그림 배열
for i in range(n):
    pict.append(list(map(int, read().split())))
visited = [[0 for _ in range(m)] for _ in range(n)] # 방문 정보를 저장할 배열(방문 하면 1, 하지 않았으면 0)

# 상하좌우 방향 배열 생셩
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0 # 그림의 개수
area = 0 # 최대 그림의 면적
max_area = 0
for row in range(n): # 행
    for col in range(m): # 열
        if pict[row][col]==1 and visited[row][col]==0: # 그림이 존재하고, 아직 방문하지 않은 경우
            cnt += 1
            area = 1
            que = deque()  # 덱 생성
            que.append((row, col))
            visited[row][col] = 1 # 방문 표시
            while que: # 큐가 비어있지 않으면
                x, y = que.popleft()
                for i in range(4): # 상하좌우 탐색
                    nx = x+dx[i] # 행 조절
                    ny = y+dy[i] # 열 조절
                    if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]==1: # 인덱스를 넘어서거나 이미 방문한 경우
                        continue
                    visited[nx][ny] = 1 # 방문 했으므로 1을 넣어줌
                    if pict[nx][ny]==1: # 주변에 그림이 있으면
                        que.append((nx, ny))
                        area += 1
            max_area = max(max_area, area)
print(cnt)
print(max_area)