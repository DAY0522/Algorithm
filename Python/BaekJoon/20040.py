# 20040번 사이클 게임
# https://www.acmicpc.net/problem/20040
import sys
read = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a: # 루트가 아닌 경우
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
parent = [i for i in range(N)]
for i in range(1, M+1):
    a, b = map(int, read().split())
    if find_parent(parent, a) == find_parent(parent, b):
        print(i)
        exit()
    union_parent(parent, a, b)
    print(parent)

print(0)