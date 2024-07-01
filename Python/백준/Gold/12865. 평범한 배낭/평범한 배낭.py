# 최대 K 담을 수 있는 배낭.
# 배낭에 넣을 수 있는 가치의 최댓값

# 현재 넣으려는 물건의 자리가 있을 때, 넣을 경우 / 안 넣을 경우 중 최댓값을 저장

import sys
read = sys.stdin.readline

N, K = map(int, read().split()) # 물건 수 / 최대 무게

data = [0]
for n in range(N):
    W, V = map(int, read().split())
    data.append((W, V)) # 무게 / 가치

dp = [[0]*(K+1) for _ in range(N+1)]

for x in range(1, N+1): # 물건
    w, v = data[x] # 현재 확인하고 있는 물품: x
    for y in range(1, K+1): # 무게
        if w <= y: # 현재 물건을 넣을 수 있는 경우
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-w] + v)
        else:
            dp[x][y] = dp[x-1][y]
print(dp[N][K])