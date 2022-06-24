# 18870번 좌표 압축
# https://www.acmicpc.net/problem/18870

N = int(input())
coord = list(map(int, input().split()))

ans = sorted(set(coord))

result = dict()
for i in range(len(ans)):
    result[ans[i]] = i

for c in coord:
    print(result[c], end=' ')