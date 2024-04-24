def find(parent, x):
    if parent[x] != x:  # root와 x가 다른 경우
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, computers):
    parent = [i for i in range(n)]
    for x in range(n):  # 위쪽 삼각형만 확인
        for y in range(n):
            if x != y and computers[x][y]:
                union(parent, x, y)

    ans = set()
    for i in range(n):
        ans.add(find(parent, i))
    return len(ans)