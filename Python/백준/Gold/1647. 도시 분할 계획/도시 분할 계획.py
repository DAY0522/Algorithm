import sys
read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
parent = [i for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, read().split())
    graph.append((c, a, b))

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = []
graph.sort()
for c, a, b in graph:
    
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer.append(c)

print(sum(answer[:-1]))