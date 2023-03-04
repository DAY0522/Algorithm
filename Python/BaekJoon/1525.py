# 1525번 퍼즐
# https://www.acmicpc.net/problem/1525

# 시간 복잡도 개선

import copy
from collections import deque

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(3):
    graph += list(map(int, input().split()))

# 초기 0 위치 찾기
for i in range(9):
    start = i
    break

visit = dict() # 이미 앞에서 나온 그래프의 경우 중복 확인
def bfs(graph):
    visit[graph] = True # 초기값 방문 체크
    que = deque([graph])
    cnt = 0
    while que:
        que_len = len(que)
        cnt += 1
        for _ in range(que_len):
            g = que.popleft()
            if g == "123456780":
                print(cnt-1)
                exit()

            pos = g.index('0') # 0 위치 반환
            for d in range(4):
                nx = pos // 3 + dx[d]
                ny  = pos % 3 + dy[d]
                if 0 <= nx < 3 and 0 <= ny < 3:
                    cur_idx = nx * 3 + ny
                    graph_copy = copy.deepcopy(list(g))
                    graph_copy[pos], graph_copy[cur_idx] = graph_copy[cur_idx], graph_copy[pos]
                    graph_str = "".join(graph_copy)
                    if visit.get(graph_str) != None:
                        continue
                    else:
                        que.append((graph_str))
                        visit[graph_str] = True

bfs("".join(map(str, graph)))
print(-1)