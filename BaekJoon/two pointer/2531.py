# 2531번 회전 초밥
import sys
read = sys.stdin.readline

N, d, k, c = map(int, read().split())
nums = [int(read()) for _ in range(N)]
nums += nums[0:k]

set_num = {}
max_val = 0
for i in range(N):
    set_num = set(nums[i:i+k])
    if not c in set_num:
        set_num.add(0)
    max_val = max(max_val, len(set_num))
print(max_val)