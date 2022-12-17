import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))
dp = [0]
for i in range(1,N+1):
    dp.append(dp[i-1]+nums[i-1])

for _ in range(M):
    i, j = map(int, read().split())
    print(dp[j]-dp[i-1])
