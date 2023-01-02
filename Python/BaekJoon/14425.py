# 14425번 문자열 집합
# https://www.acmicpc.net/problem/14425

# 주의!! 집합 S에만 같은 문자열이 없다고 했지. 검사하는 것에는 있을 수 있다.

import sys
read = sys.stdin.readline
N, M = map(int, input().split())

arr = dict()
cnt = 0

for _ in range(N):
    arr[read()] = True

for _ in range(M):
    str = read()
    if str in arr:
        cnt += 1

print(cnt)


"""
import sys
read = sys.stdin.readline
N, M = map(int, input().split())

set_A = set()
set_B = set()
list_B = list()
for _ in range(N):
    set_A.add(read().rstrip())

for _ in range(M):
    list_B.append(read().rstrip())

set_B = set(list_B)

cnt = 0
for s in set_A&set_B:
    cnt += list_B.count(s)

print(cnt)
"""