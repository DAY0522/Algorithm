# 2178번 미로 탐색
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    que = deque([(0, 0)])
    visited[0][0] = 1
    
    while que: # que is not empty
        y, x = que.popleft() # y: 행, x: 열
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<M and ny>=0 and ny<N and visited[ny][nx]==0 and graph[ny][nx]==1:
                que.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
    return visited[N-1][M-1]

if __name__ == '__main__':
    N, M = map(int, read().split()) # N: 행, M: 열
    graph = [list(map(int, read().strip())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    print(BFS())