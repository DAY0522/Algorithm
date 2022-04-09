import math

M = int(input())
N = int(input())

nums = [i**2 for i in range(math.ceil(M**(1/2)), int(N**(1/2))+1)] # M과 N 사이의 제곱수를 list로 만듦
if not nums: # nums가 비어있으면 만족하는 완전제곱수가 없는 것임
    print(-1)
else: # 비어있지 않으면 nums의 원소를 합한 값과, 최솟값(index 0)을 출력
    print(f'{sum(nums)}\n{nums[0]}')