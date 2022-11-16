# 1699번 제곱수의 합
# https://www.acmicpc.net/problem/1699

# 시간초과 발생
import math

N = int(input())
dp = [0]*(N+1)

square = [0] # 제곱수
for i in range(1, 317): # 1~100000 사이의 제곱수 저장
    square.append(i**2)

for n in range(1, N+1):
    if n**(1/2)%1==0: # 제곱수가 나머지가 없는 경우(정수인 경우)
        dp[n] = 1
        continue
    dp[n] = dp[n-1]+1
    for i in range(2, math.floor(n**(1/2))+1):
        sub = square[i] # 빼줄 제곱수 저장
        dp[n] = min(dp[n-sub]+dp[sub], dp[n])
print(dp[N])