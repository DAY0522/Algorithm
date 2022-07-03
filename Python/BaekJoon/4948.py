# https://www.acmicpc.net/problem/4948
import sys
read = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

prime = set()
for i in range(2, 123456*2+1):
    if isPrime(i):
        prime.add(i)

while True:
    cnt = 0
    n = int(input())
    if not n:
        break

    rst = set([i for i in range(n+1, 2*n+1)])

    print(len(prime & rst))