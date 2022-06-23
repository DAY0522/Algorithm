# 9241번 LCS
# https://www.acmicpc.net/problem/9251

str1 = input().strip()
str2 = input().strip()
len1, len2 = len(str1), len(str2)
dp = [0]*(len1+1)

for i in range(1, len2+1):
    max_num = 0
    for j in range(1, len1+1):
        if max_num < dp[j]:
            max_num = dp[j]
        elif str1[i-1]==str2[j-1]:
            dp[j] = max_num + 1
print(dp)