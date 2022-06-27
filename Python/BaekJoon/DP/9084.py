# 9084 동전
# https://www.acmicpc.net/problem/9084
import sys
read = sys.stdin.readline

for _ in range(int(read().strip())):
    N = int(read().strip())
    coin = list(map(int, read().split()))
    M = int(read().strip())

    dp = [1]+[0]*(M)
    for c in coin:
        for i in range(c, M+1):
            dp[i] += dp[i-c]
    print(dp[M])