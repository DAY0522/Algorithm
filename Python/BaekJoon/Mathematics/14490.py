# 14490번 백대열
# https://www.acmicpc.net/problem/14490

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)
n, m = map(int, input().split(':'))
num = gcd(n, m) # 나눠줄 수
print(n//num, end='')
print(':', end='')
print(m//num, end='')