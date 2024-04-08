def solution(brown, yellow):
    answer = []
    
    sum = brown + yellow
    for i in range(3, int((sum)**(1/2))+1):
        if sum % i == 0: # 가로가 될 가능성이 있는 i
            h = sum // i # 세로
            if (i-2)*(h-2) == yellow:
                answer = [h, i]
    
    return answer

# brown + yellow = 전체 칸의 수
# 가로 * 세로 = 전체 칸의 수
# (가로-2)*(세로-2) = yellow