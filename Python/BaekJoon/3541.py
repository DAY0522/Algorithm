# 3541번 상근타워
import sys
read = sys.stdin.readline

N, M = map(int, read().split())

def gdc(x, y): # 최대 공약수
    if y==0:
        return x
    return gdc(y, x % y)

def search_floor(num, up, down):
    div = gdc(up, down)
    floor = num % (up // div + down // div) # 이동 횟수
    cur = 0 # 현재 층
    for _ in range(floor):
        if cur >= down: # 내려갈 수 있는 경우
            cur -= down
        else: # 내려갈 수 없는 경우
            cur += up
    if cur == 0: return up+down
    return cur

ans = float('inf')
for _ in range(M):
    U, D = map(int, read().split())
    low = search_floor(N, U, D)
    if low < ans: # 최솟값 저장
        # print(ans)
        ans = low
print(ans)