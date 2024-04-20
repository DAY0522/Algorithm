# 방향성 존재

V, E = map(int, input().split())

INF = float('inf')
distance = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if (distance[i][k] + distance[k][j] < distance[i][j]):
                distance[i][j] = distance[i][k] + distance[k][j]

result = INF
for i in range(1, V+1):
    if distance[i][i] <= INF:
        result = min(result, distance[i][i])

if result < INF:
    print(result)
else: print(-1)