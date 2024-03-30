def solution(sizes):
    answer = 0
    
    w, h = 0, 0 # 더 큰 값이 w에 오도록.
    for x, y in sizes:
        if x < y: # y가 더 큰 경우
            x, y = y, x
        w = max(w, x)
        h = max(h, y)
    
    return w*h

