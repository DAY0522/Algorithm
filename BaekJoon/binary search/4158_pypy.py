# pypy로 제출하면 정답
import sys
read = sys.stdin.readline

while True:
    N, M = map(int, read().split())
    if N==0 and M==0:
        break
    li = {int(input()) for i in range(N)}&{int(input()) for i in range(M)}
    print(len(li))