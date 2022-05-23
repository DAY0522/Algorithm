# 꿀 아르바이트
n, m = map(int, input().split())
money = list(map(int, input().split()))

sum = ans = sum(money[0:m])

for st in range(n-m):
    sum -= money[st]
    sum += money[st+m]
    ans = max(ans, sum)
print(ans)

'''
# 시간 초과
n, m = map(int, input().split())
money = list(map(int, input().split()))

max_val = []
for st in range(n-(m-1)):
    max_val.append(sum(money[st:st+m]))
print(max(max_val))
'''