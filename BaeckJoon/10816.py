import sys

N = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()
candidate = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for num in candidate:
    if cnt.get(num) != None:
        print(cnt.get(num), end=" ")
    else:
        print(0, end=" ")