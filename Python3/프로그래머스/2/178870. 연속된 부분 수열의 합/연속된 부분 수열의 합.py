def solution(sequence, k):
    answer = [0, len(sequence)]
    
    s, e = 0, 0
    total = sequence[0]
    while e < len(sequence):
        if total > k:
            total -= sequence[s]
            s += 1
        elif total < k:
            e += 1
            if e < len(sequence):
                total += sequence[e]
        else:
            if e-s < answer[1] - answer[0]:
                answer = [s, e]
            total -= sequence[s]
            s += 1
            
    return answer