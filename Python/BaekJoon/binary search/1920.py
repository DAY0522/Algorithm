# 1920번 수 찾기
# https://www.acmicpc.net/problem/1920

def binary_search(nums, n):
    l = 0
    r = len(nums)-1

    while l<=r:
        mid = (l+r)//2
        if nums[mid]<n:
            l = mid+1
        elif nums[mid]>n:
            r = mid-1
        else: # 동일한 경우
            return True
    return False

N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))

for m in arr2:
    if binary_search(arr1, m):
        print(1)
    else:
        print(0)