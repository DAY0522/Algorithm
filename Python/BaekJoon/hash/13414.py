# 13414번 수강신청
# https://www.acmicpc.net/problem/13414
import sys
read = sys.stdin.readline

K, L = map(int, read().split())
stud = []
seq = {}
for i in range(L):
    id = read().strip()
    stud.append(id)
    seq[id]=i

cnt = 0
for i in range(L):
    if seq[stud[i]] == i:
        print(stud[i])
        cnt += 1
    if cnt == K:
        break