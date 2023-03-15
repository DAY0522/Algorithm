# 1238번 파티
# https://www.acmicpc.net/problem/1238
import sys
import heapq
read = sys.stdin.readline

N, M, X = map(int, read().split())
graph = [[] for _ in range(N+1)]
graph_reverse = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, read().split())
    graph[s].append((c, e))
    graph_reverse[e].append((c, s))

def dijkstra(g, start):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))

    while que: # que가 빌 때까지 반복
        cur_cost, cur_node = heapq.heappop(que)

        if cur_cost != distance[cur_node]: continue
        for new_cost, new_node in g[cur_node]:
            dist = new_cost + cur_cost
            if dist < distance[new_node]:
                heapq.heappush(que, (dist, new_node))
                distance[new_node] = dist
    return distance

ans = 0
A = dijkstra(graph, X)
B = dijkstra(graph_reverse, X)
for i in range(1, N+1):
    if ans < A[i] + B[i]:
        ans = A[i] + B[i]

print(ans)