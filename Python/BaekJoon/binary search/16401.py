# 16401번 과자 나눠주기
# https://www.acmicpc.net/problem/16401

def binary_search(start, end):
    global M

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for s in stick:
            while s >= mid:
                cnt += 1
                s -= mid

        if cnt >= M: # 더 크게 줄 수 있는 경우
            start = mid + 1
        else: # 더 작게 줘야 하는 경우
            end = mid - 1

    print(end)

M, N = map(int, input().split())
stick = list(map(int, input().split()))
if sum(stick)<M:
    print(0)
    exit()
binary_search(0, max(stick))