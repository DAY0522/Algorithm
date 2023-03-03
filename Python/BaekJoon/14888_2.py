# 14888번 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

# dfs로 풀이
N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

ans = [float('-inf'), float('inf')] # 최대, 최솟값
def dfs(n, val):
  if n == N:
    if val > ans[0]:
      ans[0] = val
    if val < ans[1]:
      ans[1] = val
    return
  else:
    if oper[0] > 0:
      oper[0] -= 1
      dfs(n+1, val+nums[n])
      oper[0] += 1
    if oper[1] > 0:
      oper[1] -= 1
      dfs(n+1, val-nums[n])
      oper[1] += 1
    if oper[2] > 0:
      oper[2] -= 1
      dfs(n+1, val*nums[n])
      oper[2] += 1
    if oper[3] > 0:
      oper[3] -= 1
      dfs(n+1, int(val/nums[n]))
      oper[3] += 1

dfs(1, nums[0])
if ans[0] == float('-inf'):
  print(ans[1])
  print(ans[1])
elif ans[1] == float('inf'):
  print(ans[0])
  print(ans[0])
else:
  print(ans[0])
  print(ans[1])