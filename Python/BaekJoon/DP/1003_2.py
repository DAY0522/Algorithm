# 1003번 피보나치 함수
# https://www.acmicpc.net/problem/1003
import sys
read = sys.stdin.readline
nums = [int(read().strip()) for _ in range(int(read().strip()))]
M = max(nums) # 가장 큰수
dp_zero = [1, 0]
dp_one = [0, 1]
for i in range(2, M+1):
    dp_zero.append(dp_zero[i-1]+dp_zero[i-2])
    dp_one.append(dp_one[i-1]+dp_one[i-2])

for n in nums:
    print(dp_zero[n], dp_one[n])