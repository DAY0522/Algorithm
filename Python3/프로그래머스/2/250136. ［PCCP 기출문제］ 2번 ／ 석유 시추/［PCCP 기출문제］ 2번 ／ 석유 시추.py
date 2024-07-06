from collections import deque
def solution(land):
    answer = 0
    
    HEIGHT, WIDTH = len(land), len(land[0])
    visited = [[0] * WIDTH for _ in range(HEIGHT)] # 몇 번째 석유 덩어리인지 기록
    count = {}
    
    cur_num = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if land[i][j] and not visited[i][j]:
                que = deque([(i, j)])
                cur_num += 1
                count[cur_num] = 1
                visited[i][j] = cur_num
                
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx >= 0 and nx < HEIGHT and ny >=0 and ny < WIDTH:
                            if land[nx][ny] and not visited[nx][ny]:
                                que.append((nx, ny))
                                visited[nx][ny] = cur_num
                                count[cur_num] += 1
    for w in range(WIDTH):
        result = set()
        for h in range(HEIGHT):
            if visited[h][w]:
                result.add(visited[h][w])
        
        cur = 0
        for r in result:
            cur += count[r]
        
        if cur > answer:
            answer = cur
        
    return answer