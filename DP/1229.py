N = int(input())

dp = [1]
i = 1
while True:
    num = dp[i-1] + 6*i - (2*i-1) # n(2n-1)
    if num > N:
        break
    dp.append(num)
    i += 1
print(dp)

# n보다 작은 육각수를 뺀 값의 최솟값 + 1