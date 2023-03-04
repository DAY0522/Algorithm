# 1525번 퍼즐
# https://www.acmicpc.net/problem/1525

import copy
from collections import deque

graph = [list(map(int, input().split())) for _ in range(3)]

# 초기 0 위치 찾기
for r in range(3):
    for c in range(3):
        if graph[r][c] == 0:
            start = (r, c)
            break
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = set() # 이미 앞에서 나온 그래프의 경우 중복 확인

def bfs(start, graph):
    que = deque([(start, graph)])
    cnt = 0
    while que:
        que_len = len(que)
        cnt += 1
        for i in range(que_len):
            pos, g = que.popleft()
            x, y = pos
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 3 and 0 <= ny < 3:
                    graph_copy = copy.deepcopy(g)
                    graph_copy[x][y], graph_copy[nx][ny] = graph_copy[nx][ny], graph_copy[x][y]
                    cur_num = make_visit(graph_copy)
                    if cur_num == 123456780:
                        print(cnt)
                        exit()

                    if cur_num in visit:
                        continue
                    else:
                        que.append(((nx, ny), graph_copy))
                        visit.add(cur_num)

def make_visit(graph):
    cur = 0
    for r in range(3):
        for c in range(3):
            cur *= 10
            cur += graph[r][c]
    return cur

cur_num = make_visit(graph)
if cur_num == 123456780:
    print(0)
    exit()
bfs(start, graph)
print(-1)