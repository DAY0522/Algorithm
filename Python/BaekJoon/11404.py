# 11404번 플로이드
# https://www.acmicpc.net/problem/11404
import sys
read = sys.stdin.readline

n = int(read().strip())
m = int(read().strip())
dp = [[float('inf')]*(n+1) for _ in range(n+1)]
pos = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, read().split())
    if c < dp[a][b]:
        dp[a][b] = c
        pos[a][b] = b

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                pos[i][j] = pos[i][k]

for d in dp[1:]:
    for i in range(1, n+1):
        if d[i] == float('inf'):
            print(0, end=' ')
        else: print(d[i], end=' ')
    print()