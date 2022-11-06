# 15988번 1, 2, 3 더하기 3
# https://www.acmicpc.net/problem/15988
import sys
read = sys.stdin.readline

arr = [int(read().strip()) for _ in range(int(read().strip()))]
M_num = max(arr) # 최댓값
dp = [0] * (M_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = dp[1]+dp[2]+1
for i in range(4,M_num+1):
    dp[i] = (dp[i-3]%1000000009+dp[i-2]%1000000009+dp[i-1]%10000000009)%1000000009

for a in arr:
    print(dp[a]%1000000009)