# 2750번 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys
read = sys.stdin.readline

def quickSort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[len(arr)//2]

    arr_l = [n for n in arr if n<pivot]
    arr_m = [n for n in arr if n==pivot]
    arr_r = [n for n in arr if n>pivot]
    return quickSort(arr_l) + arr_m + quickSort(arr_r)

nums = [int(read().strip()) for _ in range(int(read().strip()))]
for n in quickSort(nums):
    print(n)