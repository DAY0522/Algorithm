# 13414번 수강신청
# https://www.acmicpc.net/problem/13414
import sys
read = sys.stdin.readline

K, L = map(int, read().split())
stud = {read().strip():i for i in range(L)}

stud = sorted(stud.items(), key = lambda x:x[1]) # value를 기준으로 정렬

for i in range(min(K, len(stud))):
    print(stud[i][0])