# 14503번 로봇 청소기
# https://www.acmicpc.net/problem/14503
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
x, y, direc = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]

# 시계 방향 순서대로 적용
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
while True:  # 막히기 전까지 계속 반복
    if graph[x][y] == 0:  # 청소되지 않은 경우
        graph[x][y] = 2  # 현재 칸 청소
        ans += 1

    clean = True
    for d in range(1, 5):
        a = x + dx[(direc - d) % 4]
        b = y + dy[(direc - d) % 4]
        if 0 <= a < N and 0 <= b < M and graph[a][b] == 0:  # 직진 후 청소
            clean = False
            direc = (direc - d) % 4  # 방향 재설정
            x, y = a, b
            break
    if clean:  # 청소할 곳이 없는 경우
        x = x + dx[(direc - 2) % 4]
        y = y + dy[(direc - 2) % 4]
        if graph[x][y] == 1: break # 벽인 경우 종료

print(ans)