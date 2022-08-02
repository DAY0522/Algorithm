nums = input().split('-')

if len(nums)==1:
    print(sum(map(int, nums[0].split('+'))))
    exit()

nums[0] = sum(map(int, nums[0].split('+')))
for i in range(1, len(nums)):
    nums[i] = sum(map(int, nums[i].split('+')))
print(nums[0]-sum(nums[1:]))