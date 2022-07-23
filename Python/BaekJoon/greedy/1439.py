# 1439번 뒤집기
# https://www.acmicpc.net/problem/1439

seq = input()
one = seq.split('0')
zero = seq.split('1')
res1, res2 = 0, 0
for o in one: # zero를 뒤집는 경우
    if len(o): res1 += 1
for z in zero: # one을 뒤집는 경우
    if len(z): res2 += 1
print(min(res1,res2))