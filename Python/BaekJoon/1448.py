# 1448번 삼각형 만들기
# https://www.acmicpc.net/problem/1448
import sys
read = sys.stdin.readline

N = int(read().strip())
lines = [int(read().strip()) for _ in range(N)]
lines.sort()

