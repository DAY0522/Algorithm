# 24060번 알고리즘 수업 - 병합 정렬 1
# https://www.acmicpc.net/problem/24060

global ans
ans = []

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)//2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])

    # merge
    result = list()
    l, r = 0, 0
    while l < len(left_part) and r < len(right_part):
        if left_part[l] < right_part[r]:
            result.append(left_part[l])
            ans.append(left_part[l])
            l += 1
        else:
            result.append(right_part[r])
            ans.append(right_part[r])
            r += 1
    if l < len(left_part):
        while l < len(left_part):
            result.append(left_part[l])
            ans.append(left_part[l])
            l += 1
    else:
        while r < len(right_part):
            result.append(right_part[r])
            ans.append(right_part[r])
            r += 1
    return result

N, K = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr)
try:
    print(ans[K-1])
except:
    print(-1)