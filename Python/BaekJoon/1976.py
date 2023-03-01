# 1976번 여행 가자
# https://www.acmicpc.net/problem/1976
import sys
read = sys.stdin.readline

N = int(read().strip())
M = int(read().strip())
parent = [i for i in range(N+1)]

def find_parent(parent, a):
    if parent[a] != a: # 루트 노드가 아닌 경우
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, N+1):
    info = list(map(int, read().split()))
    for j in range(len(info)):
        if info[j] == 1: # 연결된 경우
            union_parent(parent, i, j+1)

plan = list(map(int, read().split()))
result = True
for i in range(M-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        break

if result: # True인 경우
    print("YES")
else: print("NO")