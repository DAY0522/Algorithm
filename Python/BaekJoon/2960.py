import copy
from collections import deque
N, K = map(int, input().split())
nums = deque(i for i in range(2, N+1))
delt = 0

while True:
    P = nums.popleft()
    delt += 1
    if delt == K:
        print(P)
        exit()

    for n in copy.deepcopy(nums): # 남은 원소들 중
        if n % P == 0: # 나누어 떨어질 시
            nums.remove(n)
            delt += 1
            if delt == K:
                print(n)
                exit()