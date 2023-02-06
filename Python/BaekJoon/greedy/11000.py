# 11000번 강의실 배정
# https://www.acmicpc.net/problem/11000
import sys
read = sys.stdin.readline

N = int(read().strip())
lect = [list(map(int, read().split())) for _ in range(N)]
bool = [False] * N

