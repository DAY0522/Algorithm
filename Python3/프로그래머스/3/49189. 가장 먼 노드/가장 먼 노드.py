# 1~n, 1에서 가장 멀리 떨어진 노드의 갯수
import heapq

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    dist = [INF] * (n+1)
    
    for a, b in edge:
        graph[a].append((b, 1)) # 도착, 비용
        graph[b].append((a, 1))
    
    q = []
    dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        
        for g in graph[now]:
            c = cost + g[1]
            if c < dist[g[0]]:
                heapq.heappush(q, (c, g[0]))
                dist[g[0]] = c

    dist = dist[1:]
    result = max(dist)
    for d in dist:
        if result == d:
            answer += 1
    
    return answer