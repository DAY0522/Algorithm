from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    idx = 0
    q = deque([0]*bridge_length)
    sum = 0
    
    while True:
        answer += 1 # 옮기기
        val = q.popleft() # 내리기
        sum -= val
        
        if idx<len(truck_weights) and truck_weights[idx] <= weight-sum: # 태우기
            q.append(truck_weights[idx])
            sum += truck_weights[idx]
            idx += 1
            if idx ==len(truck_weights):
                answer += bridge_length
                break
        else: # 못태우는 경우
            q.append(0)
    
    return answer