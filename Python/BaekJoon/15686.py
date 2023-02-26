# 15686번 치킨 배달
# https://www.acmicpc.net/problem/15686
import sys
import copy
from collections import deque
from itertools import combinations
read = sys.stdin.readline

# 브루트포스 시간초과
N, M = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
house = []
chick = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1: # 집인 경우
            house.append((r,c))
        elif graph[r][c] == 2: # 치킨집인 경우
            chick.append((r,c))

comb = combinations(chick, M) # 폐업되지 않은 치킨집의 조합
ans = float('inf')
for c in comb:
    distance = 0
    for h_x, h_y in house: # 집을 순회하면서 거리 세기
        dist = float('inf')
        for x, y in c:
            if abs(h_x-x) + abs(h_y-y) < dist:
                dist = abs(h_x-x) + abs(h_y-y)
        distance += dist
        if distance >= ans: break
    if distance < ans: # 최솟값 구하기
        ans = distance
print(ans)