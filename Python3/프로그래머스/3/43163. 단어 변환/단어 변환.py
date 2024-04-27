from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque([begin])
    visit = {begin:0}
    while q:
        now = q.popleft()
        for w in words: # 모든 단어에 대해
            if visit.get(w)==None and compare(now, w): # 방문하지 않고, 1개 글자만 차이나는 경우
                q.append(w)
                visit[w] = visit[now] + 1
    
    if target in visit:
        return visit[target]
        
    return 0

def compare(s1, s2): # 하나의 알파벳만 차이나는지 비교하는 함수
    comp = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: # 다른 경우
            comp += 1
            if comp == 2:
                return False
    return True