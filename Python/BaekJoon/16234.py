# 16234 인구 이동
# https://www.acmicpc.net/problem/16234
import sys
read = sys.stdin.readline

N, L, R = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]

while True:
	for r in 