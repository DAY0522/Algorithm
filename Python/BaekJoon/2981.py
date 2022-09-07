# 2981번 검문
# https://www.acmicpc.net/problem/2981

import sys
import math

read = sys.stdin.readline

def gcd(a, b): # a와 b의 최대공약수를 구하는 함수
    if a%b==0: # 나머지가 없는 경우
        return b
    else:
        return gcd(b, a%b)

N = int(input())
nums = list(int(input()) for _ in range(N))
nums_sub = list()

for i in range(N):
    if i == N-1:
        nums_sub.append(nums[i]-nums[0])
    else:
        nums_sub.append(nums[i+1]-nums[i])

nums_sub.sort()
prev_gcd = nums_sub[0]
for i in range(1, N):
    prev_gcd = gcd(prev_gcd, nums_sub[i])

ans = list()
for n in range(2, int(math.sqrt(prev_gcd))+1):
    if not prev_gcd % n: # 나머지가 없으면
        ans.append(n)
        ans.append(prev_gcd//n)
ans.append(prev_gcd)
ans = list(set(ans))
ans.sort()
print(*ans)

''' 메모리 초과
from collections import deque
import copy
import sys

read = sys.stdin.readline

N = []
result = [] # 결과 저장
N = [int(input()) for _ in range(int(input()))]

M_cand = deque(i for i in range(2, N[-1]-1))

while M_cand: # 후보가 없을 때까지 반복
    remd = set() # 나머지 저장
    m = M_cand.popleft()
    for n in N:
        remd.add(n%m)
        if len(remd) > 1:
            for cand in copy.deepcopy(M_cand):
                if cand % m == 0:
                    M_cand.remove(cand)
            break
    if len(remd) == 1:
        result.append(m)

for r in result:
    print(r, end=' ')
'''