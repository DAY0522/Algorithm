import sys
import copy
from itertools import combinations
from collections import deque

read = sys.stdin.readline


def change_graph(graph, pos):
    graph = copy.deepcopy(graph)
    for x, y in pos:
        graph[x][y] = 1  # 조합에서 추출된 위치를 벽으로 변경
    return graph


def dfs(virus, cnt):
    global graph, c, ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for c in comb:
        visit = [[False] * M for _ in range(N)]
        g = change_graph(graph, c)

        cur = cnt
        que = deque()  # 2가 있는 위치를 등록
        for v_x, v_y in virus:
            que.append((v_x, v_y))
            visit[v_x][v_y] = True

        while que:
            x, y = que.pop()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 0 and not visit[nx][ny]:
                    cur -= 1
                    g[nx][ny] = 2  # 감염
                    que.append((nx, ny))
                    visit[nx][ny] = True
            if cur <= ans:
                break

        if cur > ans:
            ans = cur

    return ans


N, M = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
virus = []
blank = []
cnt = 3
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:  # 빈칸
            blank.append((r, c))
        else:
            cnt += 1
            if graph[r][c] == 2:  # 바이러스
                virus.append((r, c))

cnt = N * M - cnt  # 현재 남은 벽의 개수
comb = combinations(blank, 3)  # 빈칸인 곳들 중 3개를 골라 조합 생성

ans = 0
print(dfs(virus, cnt))