# 14889번 스타트와 링크
# https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

read = sys.stdin.readline

N = int(read().strip())
part = [i for i in range(N)]
graph = [list(map(int, read().split())) for _ in range(N)]

result = float('inf')
all = set(part)
comb = list(combinations(part, N // 2))

for s in range(len(comb)):
    start = comb[s]
    link = comb[len(comb) - s - 1]
    cnt_a, cnt_b = 0, 0
    # 스타트
    for i in range(N // 2 - 1):
        s_a = start[i]
        l_a = link[i]
        for j in range(i + 1, N // 2):
            s_b = start[j]
            cnt_a += graph[s_a][s_b] + graph[s_b][s_a]

            l_b = link[j]
            cnt_b += graph[l_a][l_b] + graph[l_b][l_a]

    if abs(cnt_a - cnt_b) < result:
        result = abs(cnt_a - cnt_b)
        if result == 0:
            break

print(result)