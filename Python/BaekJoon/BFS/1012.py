# 1012번 유기농 배추
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우 배열 생성
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(read())
for t in range(T):
    w, h, k = map(int, read().split()) # width / height / 총 배추 개수
    graph = [[False for _ in range(w)] for _ in range(h)]
    visit = [[False for _ in range(w)] for _ in range(h)]
    for _ in range(k): # 배추 위치를 True 변경
        a, b = map(int, read().split()) # a: y, b: x
        graph[b][a] = True

    cnt = 0
    for row in range(h): # 행(y)
        for col in range(w): # 열(x)
            if graph[row][col] == 1 and visit[row][col] == 0: # 배추가 있고 방문을 하지 않은 경우
                cnt += 1
                que = deque([(row, col)]) # create queue with start node
                visit[row][col] = 1

                while que: # que is not empty
                    y, x = que.popleft()
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if ny >= 0 and ny < h and nx >= 0 and nx < w and graph[ny][nx] == 1 and visit[ny][nx] == 0: # 인덱스 범위를 넘어서지 않고, 그림이 있으며, 방문하지 않은 경우
                            visit[ny][nx] = 1 # 방문 표시
                            que.append((ny, nx))
    print(cnt)



