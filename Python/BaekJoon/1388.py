# 1388번 바닥 장식
# https://www.acmicpc.net/problem/1388
import sys
read = sys.stdin.readline
N, M = map(int, read().split()) # 행, 열
graph = [read().strip() for _ in range(N)]
visit = [[False]*M for _ in range(N)]

cnt = 0
for r in range(N): # 행
    for c in range(M): # 열
        if not visit[r][c]: # 방문하지 않았을 경우
            cnt += 1
            if graph[r][c] == '-': # 가로 타일이면
                next = c
                while next < M and graph[r][next]=='-':
                    visit[r][next] = True
                    next += 1
            else: # 세로 타일이면 '|'
                next = r
                while next < N and graph[next][c]=='|':
                    visit[next][c] = True
                    next += 1
print(cnt)