# 홀/짝인지에 따라 나눠야할 듯
x = int(input())
num = 0

while True:
    if x <= num*(num+1)/2:
        break
    num += 1

sum = num*(num-1)//2 + 1
if num % 2 == 0: # num이 짝수면
    frac = 1 + (x - sum)
    deno = num - (x - sum)
else: # 홀수면
    frac = num - (x - sum)
    deno = 1 + (x - sum)
print(f'{frac}/{deno}')