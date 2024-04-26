def find(parent, a):
    if parent[a] != a: # 부모가 루트 노드가 아닌 경우
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    
    graph = []
    parent = [i for i in range(n+1)]
    for a, b, cost in costs:
        graph.append((cost, a, b))
        
    graph.sort() # cost를 기준으로 정렬
    for cost, a, b in graph:
        if find(parent, a) != find(parent, b): # 사이클이 생기지 않으면
            union(parent, a, b)
            answer += cost
    
    return answer