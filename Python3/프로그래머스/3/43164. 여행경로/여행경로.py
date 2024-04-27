import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    result = [] # 모든 경로를 저장하는 리스트
    for i in range(len(tickets)):
        visited = [False] * len(tickets)
        visited[i] = True
        if tickets[i][0]=="ICN": # 시작 지점이 인천인 경우
            dfs(1, tickets[i], visited, tickets, result)
    result.sort()
    return result[0]

def dfs(n, route, visited, tickets, result):
    if n == len(tickets): # 모든 항공권을 소진한 경우
        result.append(route)
    
    for i in range(len(tickets)):
        start, end = tickets[i]
        if start == route[-1] and not visited[i]: # 이전 도착지와 새로운 출발지가 같고, 티켓을 사용하지 않은 경우
            visited[i] = True
            dfs(n+1, route+[end], visited, tickets, result)
            visited[i] = False