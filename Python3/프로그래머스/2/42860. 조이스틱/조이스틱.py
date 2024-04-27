def solution(name):
    answer = 0

    move = len(name) - 1
    for i, c in enumerate(name):
        answer += countUpDown(c)
        
        next = i+1
        while next<len(name) and name[next]=='A': # 가장 긴 A 찾기
            next += 1
        
        left = i
        right = len(name)-next
        move = min(move, 2*left+right, left+2*right)
    answer += move
    
    return answer

def countUpDown(cur): # 알파벳 선택
    up = ord(cur)-ord('A')
    down = ord('Z')-ord(cur)+1
    
    if up <= down:
        return up
    else:
        return down
    