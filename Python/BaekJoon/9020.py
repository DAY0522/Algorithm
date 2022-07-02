# 9020번 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

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
for i in range(2, 4999):
    if isPrime(i):
        prime.add(i)

T = int(input()) # test case
for _ in range(T):
    n = int(input())
    ans = False # 답이 출력이 됐는지를 나타내는 변수

    if (n/2) % 2 == 0: # 짝수인 경우
        m = n//2-1
        M = n//2+1
    else:
        m = n//2
        M = n//2

    for i in range(n//4):
        if isPrime(m-2*i) and isPrime(M+2*i):
            print(m-2*i, M+2*i)
            ans = True
            break

    if not ans: # 위 for문에서 답이 출력이 되지 않은 경우, 즉 답변에 2가 포함된 경우
        print(2, n-2)