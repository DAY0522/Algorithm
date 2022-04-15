import sys
input = sys.stdin.readline
N = int(input())
peop = [tuple(map(int, input().split())) for _ in range(N)]
grade = [1] * N
for cur in range(N):
    for cmp in peop:
        if peop[cur][0] < cmp[0] and peop[cur][1] < cmp[1]:
            grade[cur] += 1
for i in grade:
    print(i, end=' ')