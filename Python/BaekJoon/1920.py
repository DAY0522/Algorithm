def binary_search(num, size, lst):
    left = 0
    right = size-1

    while left<=right:
        mid = (left + right)//2
        if lst[mid] == num:
            return True
        if num < lst[mid]:
            right=mid-1
        if num > lst[mid]:
            left=mid+1

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    if binary_search(M_list[i], N, N_list):
        print(1)
    else:
        print(0)