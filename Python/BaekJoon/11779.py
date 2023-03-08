# 11779번 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779
import sys
import heapq
read = sys.stdin.readline

N = int(read().strip()) # 도시의 개수
M = int(read().strip()) # 버스 개수
graph = [[] for _ in range(N+1)] # 버스 정보
for _ in range(M):
    s, e, cost = map(int, read().split())
    graph[s].append((cost, e))
START, END = map(int, read().split())
route = [0 for _ in range(N+1)]
def dijkstra(start, end):
    distances = [float('inf') for _ in range(N+1)]
    distances[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while que: # heap이 빌 때까지
        cur_cost, cur_node = heapq.heappop(que)
        if cur_cost != distances[cur_node]: continue # 이미 최소비용이 구해진 값

        for new_cost, new_node in graph[cur_node]:
            d = cur_cost + new_cost
            if d < distances[new_node]:
                heapq.heappush(que, (d, new_node))
                distances[new_node] = d
                route[new_node] = cur_node
    return distances[end]

print(dijkstra(START, END))
ans = [END] # end까지의 경로
while ans[-1] != START  :
    ans.append(route[ans[-1]])
print(len(ans))
print(*ans[::-1])