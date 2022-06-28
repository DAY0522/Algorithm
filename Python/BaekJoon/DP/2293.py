# 2293번 동전 1
# https://www.acmicpc.net/problem/2293
import sys
read = sys.stdin.readline
n, k = map(int, read().split())
coins = [int(read().strip()) for _ in range(n)]
dp = [1]+[0]*k
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[k])