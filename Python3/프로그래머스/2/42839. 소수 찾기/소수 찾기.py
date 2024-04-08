from itertools import permutations

def solution(numbers):
    
    result = []
    for i in range(1, len(numbers) + 1):
        p = list(set(permutations(numbers, i))) # i개를 뽑아 순열
        
        for j in range(len(p)):
            num = int("".join(p[j]))
            if isPrime(num): # True인 경우 +1
                result.append(num)
    
    return len(set(result))

def isPrime(n): # 소수인지 확인하는 함수
    if n == 1 or n == 0:
        return False
    
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
        
    return True