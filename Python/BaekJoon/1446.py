# 1446번 지름길
# https://www.acmicpc.net/problem/1446

import sys
read = sys.stdin.readline
N, D  = map(int, read().split())

road = [list(map(int, read().split())) for _ in range(N)]
road.sort(key=lambda x:x[1])
dp = [i for i in range(D+1)]

for s, e, d in road:
    if e > D: break
    if dp[s]+d < dp[e]:
        dp[e]=dp[s]+d
        val = dp[e]
        for i in range(1, D-e+1):
            dp[e+i] = val + i

print(dp[D])