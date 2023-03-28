# 14501번 퇴사
# https://www.acmicpc.net/problem/14501
import sys
read = sys.stdin.readline
N = int(read().strip())
T = list()
P = list()
for i in range(N):
	t, p = map(int, read().split())
	T.append(t)
	P.append(p)

dp = [0 for _ in range(N+1)]
if T[N-1] == 1:
	dp[N-1] = P[N-1]

for i in range(N-2, -1, -1):
	if i+T[i] > N: # 일수를 넘는 경우
		dp[i] = dp[i+1]
	else:
		dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[0])