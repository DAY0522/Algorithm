nums = list(map(int, input().split()))

if nums[0]==nums[1] and nums[1]==nums[2]:
    print(10000+nums[0]*1000)
elif nums[0]!=nums[1] and nums[1]!=nums[2] and nums[0]!=nums[2]:
    print(max(nums)*100)
else:
    nums.sort()
    print(1000+nums[1]*100)

'''
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
'''