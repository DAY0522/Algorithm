# 2467번 용액
# https://www.acmicpc.net/problem/2467

# 이분 탐색
N = int(input())
liquid = list(map(int, input().split()))

val = 2000000000
ans = [0, 0]

for i in range(len(liquid)):
    start = i + 1
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        tmp = liquid[i] + liquid[mid]
        if abs(tmp) < val:
            val = abs(tmp)
            ans = [liquid[i], liquid[mid]]

        if tmp < 0:
            start = mid + 1
        elif tmp > 0:
            end = mid - 1
        else: # 같은 경우
            print(liquid[i], liquid[mid])
            exit()

print(ans[0], ans[1])
