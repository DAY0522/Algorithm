# 2446번 자두나무
# https://www.acmicpc.net/problem/2240
import sys
read = sys.stdin.readline

T, W = map(int, read().split())
plums = [0]+[int(read().strip()) for _ in range(T)]
dp = [[0]*(T+1) for _ in range(W+1)] # 각 지점에서의 최대 자두 개수
cnt = [0]*(W+1) # 동일 나무에서 이어 먹을 때의 이전 자두의 최대 개수

for c in range(1, T+1):
    if plums[c]==1:
        cnt[0] += 1
        dp[0][c] = cnt[0]

for r in range(1, W+1):
    for c in range(1, T+1):
        if r%2==0 and plums[c]==1: # 나무 1에서 받아야 하는 경우
            dp[r][c] = max(cnt[r], dp[r-1][c-1])+1
            cnt[r] = dp[r][c]
        elif r%2==1 and plums[c]==2: # 나무 2에서 받아야 하는 경우
            dp[r][c] = max(cnt[r], dp[r-1][c-1])+1
            cnt[r] = dp[r][c]
print(max(cnt))