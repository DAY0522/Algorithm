# 9252번 LCS2
# https://www.acmicpc.net/problem/9252

str1 = input().strip()
str2 = input().strip()
len1, len2 = len(str1), len(str2)
dp = [[0]*(len1+1) for _ in range(len2+1)]

for i in range(1, len2+1): #str2
    for j in range(1, len1+1): #str1
        if str1[j-1]==str2[i-1]: #문자열이 같은 경우
            dp[i][j] = dp[i-1][j-1]+1
        else: #같지 않은 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len2, len1
seq = []
while i>0 and j>0:
    if str1[j-1]==str2[i-1]:
        seq.append(str1[j-1])
        i -= 1
        j -= 1
    else: # 더 큰 값 찾아가기
        if dp[i-1][j] < dp[i][j-1]:
            j -= 1
        else:
            i -= 1
print(dp[len2][len1])
for s in seq[::-1]:
    print(s, end='')