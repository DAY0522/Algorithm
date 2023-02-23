# 1043번 거짓말
# https://www.acmicpc.net/problem/1043
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, read().split())
parent = [i for i in range(N+1)]
true = list(map(int, read().split()))
if true[0]==0:
    print(M)
    exit()
true = true[1:]

party = list()
visit = [False]*(N+1)
for _ in range(M):
    p = list(map(int, read().split()))
    party.append(p[1:])
    for i in range(1, len(p)-1):
        visit[p[i]] = True
        union_parent(parent, p[i], p[i+1])
    visit[p[-1]] = True

ans = 0
result = list()
for t in true:
    result.append(t)
    result.append(parent[t])
result = list(set(result))

for p in party:
    check = True
    for i in range(len(p)):
        if find_parent(parent, parent[p[i]]) in result:
            check = False
            break
    if check: ans += 1
print(ans)