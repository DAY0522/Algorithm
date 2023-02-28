# 2467 용액
# https://www.acmicpc.net/problem/2467

# 투 포인터
N = int(input())
liquid = list(map(int, input().split()))

def binary_search(start, end):

    val = 2000000000
    ans = [0, 0]
    while start < end:
        if abs(liquid[start]+liquid[end]) < val:
            val = abs(liquid[start]+liquid[end])
            ans = [liquid[start], liquid[end]]

        if liquid[start]+liquid[end] < 0:
            start += 1
        elif liquid[start]+liquid[end] > 0:
            end -= 1
        else: # 같은 경우
            print(liquid[start], liquid[end])
            return True
    print(*ans)
    return True

binary_search(0, N-1)
