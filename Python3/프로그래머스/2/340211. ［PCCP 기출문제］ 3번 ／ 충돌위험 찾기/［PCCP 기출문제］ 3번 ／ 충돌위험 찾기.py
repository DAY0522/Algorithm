# (r,c) 2차원 좌표 n개 존재
# 로봇의 운송 경로 m개
# x대

def solution(points, routes):
    answer = 0
    
    result = dict()
    for route in routes:
        t = 0
        for i in range(len(route)-1):
            start_x, start_y = points[route[i]-1]
            end_x, end_y = points[route[i+1]-1]
            
            if t==0:
                try:
                    result[(start_x, start_y, t)] += 1
                except:
                    result[(start_x, start_y, t)] = 1
                    
            while start_x != end_x:
                t += 1
                if start_x > end_x:
                    start_x -= 1
                else:
                    start_x += 1
                try:
                    result[(start_x, start_y, t)] += 1
                except:
                    result[(start_x, start_y, t)] = 1
            
            while start_y != end_y:
                t += 1
                if start_y > end_y:
                    start_y -= 1
                else:
                    start_y += 1
                try:
                    result[(start_x, start_y, t)] += 1
                except:
                    result[(start_x, start_y, t)] = 1
    for point, cnt in result.items():
        if cnt >= 2:
            answer += 1
    
    return answer