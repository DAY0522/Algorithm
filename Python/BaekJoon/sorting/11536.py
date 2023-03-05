# 11536번 줄 세우기
# https://www.acmicpc.net/problem/11536
import sys
read = sys.stdin.readline

N = int(read().strip())
names = [read().strip() for _ in range(N)]

if names[0] < names[1]: # 오름차순
    for i in range(1, N-1):
        if names[i] > names[i+1]:
            print("NEITHER")
            exit()
    print("INCREASING")
else: # 내림차순
    for i in range(1, N-1):
        if names[i] < names[i + 1]:
            print("NEITHER")
            exit()
    print("DECREASING")