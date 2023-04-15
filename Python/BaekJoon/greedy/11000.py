# 11000번 강의실 배정
# https://www.acmicpc.net/problem/11000
import sys
read = sys.stdin.readline

N = int(read().strip())
lecture = [list(map(int, read().split())) for _ in range(N)]
time = [] # 각 강의실의 마지막 강의 시간

lecture.sort(key=lambda x:(x[1], x[0]))
print(lecture)