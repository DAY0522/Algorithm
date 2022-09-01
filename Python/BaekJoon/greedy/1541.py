# 최소값이 되기 위해선 -뒤에 모든 +를 묶어 빼주어야 함.
exp = input().split('-')

result = sum(map(int, exp[0].split('+'))) # 첫번째 원소는 무조건 +이므로 합해서 넣어줌
for i in range(1, len(exp)):
    result -= sum(map(int, exp[i].split('+')))
print(result)

"""
sum=0
for i in exp[0].split('+'):
    sum+=int(i)

for i in exp[1:]:
    for j in i.split('+'):
        sum-=int(j)
print(sum)
"""