# 1021번 회전하는 큐
# https://www.acmicpc.net/problem/1021

from collections import deque

N, M = map(int, input().split())
dec = deque([i for i in range(1, N+1)])
nums = deque(map(int, input().split()))

cnt = 0
while nums:
    p = nums.popleft()
    p_l = dec.index(p) # 2번 연산 시 횟수
    p_r = len(dec) - p_l # 3번 연산 시 횟수

    if p_l < p_r: # 왼쪽으로 이동
        dec.rotate(-p_l)
        dec.popleft()
        cnt += p_l
    else:
        dec.rotate(p_r)
        dec.popleft()
        cnt += p_r

print(cnt)
