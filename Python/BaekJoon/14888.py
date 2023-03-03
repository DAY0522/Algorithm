# 14888번 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

# 완전 탐색
from itertools import permutations
N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
o = []
for i in range(4):
  for _ in range(oper[i]):
    if i == 0:
      o.append('+')
    elif i == 1:
      o.append('-')
    elif i == 2:
      o.append('*')
    elif i == 3:
      o.append('/')

perm = permutations(o, N-1)
ans = [float('-inf'), float('inf')]
oper = list(set(list(perm)))
for op in oper:
  cur = nums[0]
  for i in range(N-1):
    if op[i] == '+':
      cur += nums[i+1]
    elif op[i] == '-':
      cur -= nums[i+1]
    elif op[i] == '*':
      cur *= nums[i+1]
    elif op[i] == '/':
      if cur < 0:
        cur = -cur
        cur //= nums[i+1]
        cur = - cur
      else:
        cur //= nums[i+1]
  if cur > ans[0]:
    ans[0] = cur
  if cur < ans[1]:
    ans[1] = cur

if ans[0] == float('-inf'):
  print(ans[1])
  print(ans[1])
elif ans[1] == float('inf'):
  print(ans[0])
  print(ans[0])
else:
  print(ans[0])
  print(ans[1])