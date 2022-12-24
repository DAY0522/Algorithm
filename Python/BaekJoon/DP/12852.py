# 12852번 1로 만들기 2
# https://www.acmicpc.net/problem/12852

N = int(input())
dp = [0] * (N+1)
seq = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    seq[i] = i-1
    if i%3==0 and dp[i//3]+1<dp[i]:
        dp[i] = dp[i//3]+1
        seq[i] = i//3
    if i%2==0 and dp[i//2]+1<dp[i]:
        dp[i] = dp[i//2]+1
        seq[i] = i//2

print(dp[N])
ans = N
while ans:
    print(ans, end=' ')
    ans = seq[ans]
