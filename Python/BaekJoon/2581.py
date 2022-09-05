# https://www.acmicpc.net/problem/2581
M = int(input())
N = int(input())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

sum = 0
min = 0 # 최솟값이 출력된 경우 해당 값을 저장, 아닌 경우 0
for i in range(M, N+1):
    if isPrime(i): # True인 경우
        sum += i
        if not min:
            min = i

if not min:
    print(-1)
    exit()

print(sum)
print(min)