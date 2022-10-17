# 14002 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002

N = int(input())
arr = list(map(int, input().split()))

dp = [1]*N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

ans = max(dp)
print(ans)
result = []
for n in range(N-1, -1, -1):
    if dp[n]==ans:
        result.append(arr[n])
        ans -= 1

print(*result[::-1])