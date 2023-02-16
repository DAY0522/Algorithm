# 3187번 양치기 꿍
# https://www.acmicpc.net/problem/3187
import sys
from collections import deque
read = sys.stdin.readline

def bfs(x, y):
    que = deque([(x, y)])
    visit[x][y] = True
    v_cnt, k_cnt = 0, 0  # 늑대, 양

    while que:
        p_x, p_y = que.popleft()
        val = graph[p_x][p_y]
        if val == 'v':
            v_cnt += 1
        elif val == 'k':
            k_cnt += 1

        for d in range(4):
            nx = p_x + dx[d]
            ny = p_y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and graph[nx][ny] != '#':
                que.append((nx, ny))
                visit[nx][ny] = True

    if k_cnt > v_cnt:
        ans[0] += k_cnt
    else:
        ans[1] += v_cnt

R, C = map(int, read().split())
graph = [list(read().strip()) for _ in range(R)]
visit = [[False]*(C) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = [0, 0]
for r in range(R):
    for c in range(C):
        cur = graph[r][c]
        if not visit[r][c] and (cur == 'v' or cur == 'k'):
            bfs(r, c)

print(*ans)