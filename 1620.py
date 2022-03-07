import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = dict()

for n in range(1, N+1):
    name = input().strip()
    names[n] = name
    names[name] = n

for m in range(M):
    info = input().strip()
    if info.isnumeric():
        print(names[int(info)])
    else:
        print(names[info])