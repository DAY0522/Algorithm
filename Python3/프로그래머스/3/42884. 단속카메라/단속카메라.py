# 단속용 카메라를 한 번은 만나도록 카메라 설치
# 카메라의 최소 개수

def solution(routes):
    answer = 1
    
    routes.sort()
    start, end = routes[0]
    for s, e in routes[1:]:
        # print(f'-- {s, e} 확인 --')
        if s <= end:
            # print(f'{start, end} 내에 있음!')
            start = s
            if e < end:
                end = e
        else:
            # print(f'{start, end} 내에 있지 않음!')
            start = s
            end = e
            answer += 1
    return answer