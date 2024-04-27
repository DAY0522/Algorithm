# 과자 나눠주기
def binary_search(start, end):
    global result

    while start <= end:
        num = 0 # 과자 갯수
        mid = (start+end) // 2

        for l in length:
            num += l // mid
        
        if num < M: # 조카 수 보다 작은 경우(과자 크기를 줄여야 함)
            end = mid - 1
        else: # 더 많거나 같은 경우(과자 크기를 늘려야 함)
            start = mid + 1
            result = mid
        # print(f'mid: {mid}, 과자 개수: {num}')

    return mid


M, N = map(int, input().split())
length = list(map(int, input().split()))
result = 0
binary_search(1, max(length))
print(result)