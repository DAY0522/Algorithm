from itertools import combinations
from collections import deque
def checkDS(comb): # 4번 조건을 만족하는지 체크.
    S = 0
    for x, y in comb:
        if stud[x][y]=='S':
            S += 1
    return True if S>=4 else False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def chectConnect(comb): # 2번 조건을 만족하는지 체크.
    visited = [False] * 7
    que = deque()
    que.append(comb[0])
    visited[0] = True
    while que:
        x, y = que.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) in comb:
                v = comb.index((nx,ny))
                if 0<=nx<5 and 0<=ny<5 and not visited[v]:
                    que.append((nx,ny))
                    visited[v] = True

    if visited.count(False):
        return False
    return True


stud = [list(map(str,input().strip())) for _ in range(5)]
pos = [(i,j) for i in range(5) for j in range(5)]
combs = combinations(pos, 7)

ans = 0
for comb in combs:
    if checkDS(comb): # 4번 조건을 만족하는 경우
        if chectConnect(comb): # 2번 조건을 만족하는 경우
            ans += 1
print(ans)