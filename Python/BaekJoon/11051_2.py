# 11051번 이항 계수 2
# https://www.acmicpc.net/problem/11051

# Method 2: 메모이제이션(DP) 이용
N, K = map(int, input().split())
K_min = min(K, N-K)

dp = [[1]*(N+1) for _ in range(K_min+1)]
for k in range(1, K_min+1):
    for n in range(2, N+1):
        if k > n:
            continue
        elif k == n:
            dp[k][n] = 1
            continue
        dp[k][n] = dp[k-1][n-1] + dp[k][n-1]

print(dp[K_min][N] % 10007)