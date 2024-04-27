def solution(n, times):
    max_time = max(times) * n
    answer = binary_search(1, max_time, times, n)
    return answer

def binary_search(start, end, times, n):
    result = float('inf')
    while start <= end:
        mid = (start+end)//2 # 모든 사람이 심사를 받는데 걸리는 시간
        num = 0 # 탐색 받은 사람의 수
        for t in times:
            num += mid // t
        # print(f'mid: {mid}, num: {num}')
        if num < n : # 기존 사람보다 적게 확인한 경우
            start = mid + 1 # 시간을 늘려야 함.
        else: # 기존 사람보다 많이 확인한 경우
            end = mid - 1 # 시간을 줄여야 함.
            if mid < result:
                result = mid
    
    return result