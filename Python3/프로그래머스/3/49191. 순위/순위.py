def solution(n, results):
    answer = 0
    
    INF = int(1e9)
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        dist[a][b] = 1
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] >= INF and dist[j][i] < INF:
                dist[i][j] = -dist[j][i]
    for i in range(1, n+1): # i가 순위를 알 수 있는지 확인
        count = 0
        for j in range(1, n+1):
            if dist[j][i] < INF:
                count += 1
        
        # print(f'{i} 확인, {count}')
        
        if count == n-1:
            answer += 1
        
    return answer