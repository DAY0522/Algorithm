from collections import deque

def solution(edges):
    graph = {}
    nodes = set() # 모든 노드
    end = set() # 간선이 들어오는 노드
    visited = {}
    for s, e in edges:
        nodes.add(s)
        nodes.add(e)
        end.add(e)
        
        visited[s] = False
        visited[e] = False
        try:
            graph[s].append(e)
        except:
            graph[s] = [e]
    
    # 시작점 찾기
    for n in nodes:
        if n not in end:
            if len(graph[n]) > 1:
                start = n
    answer = [start, 0, 0, 0]
                
    # 시작점을 기준으로 그래프 탐색
    for v in graph[start]:
        stack = deque([v])
        visited[v] = True
        n, e = 1, 0
        while stack: # DFS
            current = stack.popleft()
            if graph.get(current) != None:
                for g in graph[current]:
                    e += 1
                    if not visited[g]:
                        n += 1
                        visited[g] = True
                        stack.append(g)
        answer[graph_type(n, e)] += 1
            
    return answer

def graph_type(node, edge):
    if node == edge: # 노드와 간선의 수가 동일한 경우 -> 도넛 모양
        return 1
    elif node == edge+1: # 막대 모양
        return 2
    elif node+1 == edge: # 8자 모양
        return 3
    
    print("error")
    return 0