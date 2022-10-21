# 7795번 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
import sys
from collections import deque
read = sys.stdin.readline

for t in range(int(read().strip())):
    N, M = map(int,read().split())
    ans = 0
    A = [0]+sorted(list(map(int,read().split())))
    B = sorted(list(map(int,read().split())))
    b = 0
    a = 1
    while a<N+1:
        val = A[a]
        while val>B[b]:
            b += 1
            if b==M:
                ans += b * (N - a)
                a = N
                break
        ans += b
        a += 1
    print(ans)