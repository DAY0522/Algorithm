# 2563번 색종이
# https://www.acmicpc.net/source/52027191
import sys
read = sys.stdin.readline

paper = list()
for _ in range(100):
    paper.append([False] * 100)

for _ in range(int(input())):
    W, H = map(int, read().split())
    for i in range(10):
        for j in range(10):
            paper[H+i][W+j] = True

cnt = 0
for p in paper:
    cnt += p.count(True)
print(cnt)