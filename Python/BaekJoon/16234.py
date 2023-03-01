# 16234 인구 이동
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
read = sys.stdin.readline

N, L, R = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
	ans = 0
	while True:
		change = False
		ans += 1
		visit = [[False] * N for _ in range(N)]
		for r in range(N):
			for c in range(N):
				if not visit[r][c]:  # 이전에 방문하지 않은 경우
					cur = [graph[r][c], 1]  # 값 / 개수
					pos = [(r, c)]  # 선택된 것들의 위치
					visit[r][c] = True
					que = deque()
					for d in range(4):
						nx = r + dx[d]
						ny = c + dy[d]
						if 0 <= nx < N and 0 <= ny < N and L <= abs(graph[r][c] - graph[nx][ny]) <= R and not visit[nx][
							ny]:
							change = True
							que.append((nx, ny))
							pos.append((nx, ny))
							visit[nx][ny] = True
							cur[0] += graph[nx][ny]
							cur[1] += 1

					while que:  # que가 빌 때까지
						x, y = que.popleft()
						for d in range(4):
							nx = x + dx[d]
							ny = y + dy[d]
							if 0 <= nx < N and 0 <= ny < N and L <= abs(graph[x][y] - graph[nx][ny]) <= R and not \
							visit[nx][ny]:
								que.append((nx, ny))
								pos.append((nx, ny))
								visit[nx][ny] = True
								cur[0] += graph[nx][ny]
								cur[1] += 1
					for x, y in pos:
						graph[x][y] = cur[0] // cur[1]

		if not change:  # 변한 게 없는 경우
			break
	return ans-1

print(bfs())