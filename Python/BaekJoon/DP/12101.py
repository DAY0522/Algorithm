# 12101번 1, 2, 3 더하기 2
# https://www.acmicpc.net/problem/12101
N, K = map(int, input().split())
dp = [''] + [[] for _ in range(N)]
dp[1].append('1')
if N>=2:
    dp[2].append('1+1')
    dp[2].append('2')

    if N>=3:
        for i in range(1, 3):
            for prev in dp[3-i]:
                dp[3].append(prev+'+'+str(i))
        dp[3].append('3')

        for cur in range(4, N+1):
            for i in range(1, 4):
                for prev in dp[cur-i]:
                    dp[cur].append(prev+'+'+str(i))

if len(dp[N]) < K: print(-1)
else: print(sorted(dp[N])[K-1])