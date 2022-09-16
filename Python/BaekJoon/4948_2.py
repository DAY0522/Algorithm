# https://www.acmicpc.net/problem/4948
# python으로 제출 시 시간 초과

import sys
read = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


while True:
    cnt = 0
    n = int(input())
    if not n:
        break

    for i in range(n+1, 2*n+1):
        if isPrime(i):
            cnt += 1

    print(cnt)
