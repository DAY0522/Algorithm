# 15486 퇴사 2
# https://www.acmicpc.net/problem/14501

# 앞에서부터 접근하는 방법
# 14501번 코드 제출해도 통과
import sys
read = sys.stdin.readline
N = int(read().strip())
T, P = [0], [0]
for i in range(1, N+1):
    t, p = map(int, read().split())
    T.append(t)
    P.append(p)

dp = [0]*(N+6)
for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])
    end = i+T[i]-1
    if end<=N:
        dp[end] = max(dp[end], P[i]+dp[i-1])
print(max(dp))