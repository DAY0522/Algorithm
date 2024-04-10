# 각각의 전력망 네트워크에서 송전탑 개수를 최대한 비슷하게 맞추고자 함.
# 모든 전선들을 한 번씩 끊으면서, 개수 확인(a)
# 개수 확인(a) 과정에서 한 네트워크에서만 개수를 확인하면 나머지 개수는 9-n이 됨!

from collections import deque

def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        visit = [False] * (n+1)
        # print(f'{i}번째 제거!')
        for j in range(len(wires)):
            if i != j:
                graph[wires[j][0]].append(wires[j][1])
                graph[wires[j][1]].append(wires[j][0])
        
        # print(graph)
        stack = deque([1])
        visit[1] = True
        res = 1
        while stack:
            # print(f'  stack값: {stack}')
            cur = stack.popleft()
            for g in graph[cur]:
                if not visit[g]:
                    stack.append(g)
                    visit[g] = True
                    res += 1
        
        sub = int(((res - (n-res))**2)**(1/2))
        # print(f'  제거 결과: {cur}, 차이: {sub}')
        
        if sub < answer:
            answer = sub
        
    return answer