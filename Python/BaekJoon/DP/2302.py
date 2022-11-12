# 2302번 극장 좌석
# https://www.acmicpc.net/problem/2302
import sys
read = sys.stdin.readline

N = int(read().strip())
dp = [0]*(N+1)
dp[1]=1
if N==1:
    print(1)
    exit()
dp[2]=2
for i in range(3, N+1):
    dp[i] = dp[i-1]+dp[i-2]

ans = 1
M = int(read().strip())
fixed = [0] + [int(read().strip()) for _ in range(M)] + [N+1]
for i in range(1,M+2):
    if fixed[i]-fixed[i-1]-1 == 0:
        continue
    ans *= dp[fixed[i]-fixed[i-1]-1]
print(ans)