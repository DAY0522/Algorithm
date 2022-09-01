# 코테 스터디 22.03.20
n = int(input())

if n == 0 or n == 1:
    print(1)
else:
    calls = [1] * (n+1)
    for i in range(2, n+1):
        calls[i] = 1 + calls[i-2] + calls[i-1]
    print(calls[n] % 1000000007)

'''
승우 코드
import sys
n = int(sys.stdin.readline())
dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] += dp[i - 1] + dp[i - 2]

print(dp[n] % 1000000007)
'''