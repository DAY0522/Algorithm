# 시간 초과
import sys
read = sys.stdin.readline

while True:
    N, M = map(int, read().split())
    if N==0 and M==0:
        break
    cd_a = [int(read()) for _ in range(N)]
    cd_b = [int(read()) for _ in range(M)]

    cnt = 0
    for target in cd_b:
        left = 0
        right = N-1

        while left <= right:
            mid = (left + right) // 2
            if target == cd_a[mid]:
                cnt += 1
                break
            elif target > cd_a[mid]:
                left = mid + 1
            else:
                right = mid - 1
    print(cnt)