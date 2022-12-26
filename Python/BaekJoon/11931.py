import sys
read = sys.stdin.readline

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[len(arr)//2]
    arr_left = [n for n in arr if n<pivot]
    arr_m = [n for n in arr if n==pivot]
    arr_right = [n for n in arr if n>pivot]
    return quick_sort(arr_right) + arr_m + quick_sort(arr_left)

arr = [int(read().strip()) for _ in range(int(read().strip()))]
arr = quick_sort(arr)
for num in arr:
    print(num)