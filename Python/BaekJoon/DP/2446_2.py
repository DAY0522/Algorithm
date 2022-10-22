# 2446번 자두나무
# https://www.acmicpc.net/problem/2240
import sys
read = sys.stdin.readline

T, W = map(int, read().split())
plums = [0]+[int(read().strip()) for _ in range(T)]
dp = [[0]*(T+1) for _ in range(W+1)] # 각 지점에서의 최대 자두 개수

for c in range(1, T+1):
    if plums[c]==1: # 나무 1
        dp[0][c] = dp[0][c-1] + 1 # 자두 하나 추가
    else: # 나무 2
        dp[0][c] = dp[0][c-1] # 이전 값 그대로 넣어줌

for r in range(1, W+1):
    for c in range(1, T+1):
        if r%2==0 and plums[c]==1: # 나무 1에서 받아야 하는 경우
            dp[r][c] = max(dp[r][c-1], dp[r-1][c-1])+1
        elif r%2==1 and plums[c]==2: # 나무 2에서 받아야 하는 경우
            dp[r][c] = max(dp[r][c-1], dp[r-1][c-1])+1
        else: # 현재 나무   에 가만히 있을 때 자두를 못 먹는 경우
            dp[r][c] = max(dp[r][c-1], dp[r-1][c-1])

m = 0
for d in dp:
    m = max(m, d[-1])
print(m)