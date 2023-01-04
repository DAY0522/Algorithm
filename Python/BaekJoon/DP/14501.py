# 14501번 퇴사
# https://www.acmicpc.net/problem/14501

# 뒤에서부터 접근
# 앞에서부터 접근하는 방법은 15486 참고
import sys
read = sys.stdin.readline
N = int(read().strip())
T, P = [0], [0]
for i in range(1, N+1):
    t, p = map(int, read().split())
    T.append(t)
    P.append(p)

dp = [0]*(N+6) # i번째 일에 상담 시 얻을 수 있는 최대 수익
for i in range(N, 0, -1):
    if i+T[i]>N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
print(dp[1])