import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
dec = deque([i for i in range(1, n+1)])
result = []
term = []

past = 0
for i in num:
    if not len(dec) == 0:
        if i >= dec[0]:
            while dec[0] <= i:
                result.append(dec.popleft())
                term.append('+')
                if not dec:
                    break
    if not result:
        print("NO")
        exit()
    while result[-1] >= i:
        result.pop()
        term.append('-')
        if not result:
            break

for t in term:
    print(t)

# 이전 것보다 더 큰 거 가능
# 작은 거는 바로 아래 있는 거 가능.
# 정렬해서 바로 이전 인덱스에 있는 거면 가능.

# 딕셔너리 이용
# pop 되면 해당 숫자 value -1씩 함
# 만약 2번 이상 pop되면 문제 있는 것임