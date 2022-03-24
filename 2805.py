import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

while left <= right:
    sum = 0
    mid = (left+right)//2
    for i in trees:
        if i > mid:
            sum += i-mid
    if sum >= M:
        left = mid+1
    else:
        right = mid-1
print(right)