# 1904번 01타일
# https://www.acmicpc.net/problem/1904

N = int(input())
dp = [1]*2 + [0]*(N-1)
for i in range(2, N+1):
    dp[i] = (dp[i-1]%15746+dp[i-2]%15746)%15746
print(dp[N])