# 9241번 LCS
# https://www.acmicpc.net/problem/9251

str1 = input().strip()
str2 = input().strip()
len1, len2 = len(str1), len(str2)
dp = [[0]*(len1+1) for _ in range(len2+1)]

for i in range(1, len2+1):
    for j in range(1, len1+1):
        if str1[j-1]==str2[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else: # 같지 않은 경우
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len2][len1])