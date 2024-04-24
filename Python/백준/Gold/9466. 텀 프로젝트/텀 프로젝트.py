import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global result  # result 변수를 함수 내부에서 수정하기 위해 global 선언
    visited[x] = True # 현재 노드 방문처리
    cycle.append(x)

    nxt = person[x] # x가 가리키는 학생
    if visited[nxt]: # 방문하지 않은 경우
        if nxt in cycle: # 가리키는 학생이 cycle에 존재하는 경우
            result += cycle[cycle.index(nxt):] # 사이클 내에 있는 학생 집합에 추가
        return
    else:
        dfs(nxt)

for _ in range(int(read().strip())):
    n = int(read().strip())
    person = [0] + list(map(int, read().split()))

    result = [] # 사이클이 발생하는 학생 집합

    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]: # 아직 방문하지 않은 경우
            cycle = [] # 사이클 발생한 학생 집합(순서 보장)
            dfs(i)
            
    
    print(n-len(result))
