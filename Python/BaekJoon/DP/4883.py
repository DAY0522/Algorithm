# 4883번 삼각 그래프
# https://www.acmicpc.net/problem/4883
import sys
read = sys.stdin.readline
test = 1
while True:
    N = int(read().strip())
    if N == 0: exit()
    graph = [list(map(int,read().split())) for _ in range(N)]
    graph[0][0]=1001
    graph[0][2]+=graph[0][1]
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = graph[0]

    for r in range(1, N):
        dp[r][0] = graph[r][0] + min(dp[r-1][0], dp[r-1][1])
        dp[r][1] = graph[r][1] + min(dp[r-1][0], dp[r-1][1], dp[r-1][2], dp[r][0])
        dp[r][2] = graph[r][2] + min(dp[r-1][1], dp[r-1][2], dp[r][1])
    print(f'{test}. {dp[-1][1]}')
    test += 1