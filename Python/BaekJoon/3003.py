# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

default = [1, 1, 2, 2, 2, 8]
DH = list(map(int, input().split()))

for i in range(6):
    print(default[i]-DH[i], end=' ')