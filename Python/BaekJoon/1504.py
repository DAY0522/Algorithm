# 1504번 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
import sys
import heapq
read = sys.stdin.readline

N, E = map(int, read().split())
graph =[[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, read().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(g, start):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while que:
        cur_cost, cur_node = heapq.heappop(que) # pop
        if cur_cost != distance[cur_node]: continue

        for new_cost, new_node in g[cur_node]:
            d = new_cost + cur_cost
            if d < distance[new_node]:
                heapq.heappush(que, (d, new_node))
                distance[new_node] = d
    return distance

v1, v2 = map(int, read().split())
start_dijk = dijkstra(graph, 1)
v1_dijk = dijkstra(graph, v1)
v2_dijk = dijkstra(graph, v2)

ans = min(start_dijk[v1]+v1_dijk[v2]+v2_dijk[N], start_dijk[v2]+v2_dijk[v1]+v1_dijk[N])
if ans == float('inf'): print(-1)
else: print(ans)