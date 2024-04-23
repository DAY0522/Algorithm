def solution(citations):
    answer = 0
    
    citations.sort() # 정렬
    
    for h in range(0, citations[-1]+1): # 가장 작은 것부터, 가장 큰 거까지
        cnt = 0
        for i in range(0, len(citations)): # 인덱스 순회
            if citations[i] < h: # h 미만 인용된 논문
                cnt += 1
            else:
                break
        if len(citations)-cnt>=h and cnt<=h:
            answer = h
    
    return answer