# 1822번 차집합
# https://www.acmicpc.net/problem/1822

A, B = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

ans = A_set-B_set
if len(ans):
    print(len(ans))
    print(*(sorted(list(ans))))
else:
    print(0)