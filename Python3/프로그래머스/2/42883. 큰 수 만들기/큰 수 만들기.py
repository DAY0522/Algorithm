def solution(number, k):
    answer = [] # stack
    
    for num in number:
        if not answer: # answer가 비어있는 경우
            answer.append(num)
            continue
        
        while k>0 and answer[-1] < num: # 이후에 오는 숫자가 더 큰경우
            answer.pop() # 이전 숫자 제거
            k -= 1 # 하나 제거 했으므로 k-1
            if not answer:
                break
        answer.append(num)
    
    answer = answer[:-k] if k>0 else answer
        
    return "".join(answer)