# 2468번 안전 영역
import sys
from collections import deque
read = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
            
def BFS(sub):
    cnt = 0
    for row in range(N):
        for col in range(N):
            if graph[row][col]>sub and visited[row][col]==0:
                cnt += 1
                que = deque([(row, col)])
                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx >= 0 and nx < N and ny >= 0 and ny < N and graph[ny][nx]>sub and visited[ny][nx]==0:
                            que.append((ny, nx))
                            visited[ny][nx] = 1
    return cnt

if __name__ == '__main__':
    N = int(read())
    graph = [list(map(int, read().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    val = 1
    max_h = max(map(max, graph))
    for i in range(1, max_h):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        val = max(val, BFS(i))
    print(val)