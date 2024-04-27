import heapq

def solution(jobs):
    answer = 0
    
    cur = 0 # 끝 지점
    q = []
    for i, j in jobs:
        heapq.heappush(q, (i, j))
        
    while q:
        remain = [] # 실행되지 않은 것들을 저장
        if q[0][0] <= cur:
            while q and q[0][0] <= cur: # 실행될 수 있는 경우
                start, dist = heapq.heappop(q)
                heapq.heappush(remain, (dist, start))
            # 가장 dist가 작은 것을 실행
            dist, start = heapq.heappop(remain)
            answer += dist + (cur-start)
            cur += dist
            while remain:
                dist, start = heapq.heappop(remain)
                heapq.heappush(q, (start, dist))   
        else:
            start, dist = heapq.heappop(q)
            answer += dist
            cur = start + dist
    
    return answer // len(jobs)