# 1932번 정수 삼각형
# https://www.acmicpc.net/problem/1932
import sys
read = sys.stdin.readline
N = int(read().strip())
tri = [list(map(int, read().split())) for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
print(tri[0][0])