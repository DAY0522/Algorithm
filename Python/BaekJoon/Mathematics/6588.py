# 6588번 골드바흐의 추측
# https://www.acmicpc.net/problem/6588

# 합이 n인 두 소수를 찾을 때 모든 소수 쌍을 시도하면 안 됩니다.
# 시간 복잡도에 대해 배우면 이 방법이 O(n^2)의 시간이 걸린다는 것을 알 수 있습니다. 소수 p를 선택하면 나머지 하나는 n-p여야 한다는 점을 활용해 보세요.

import sys
read = sys.stdin.readline

def prime_seq(num):
    prime = [False]*2 + [True for _ in range(num-1)]

    for i in range(2, num):
        if prime[i]: # True면 배수 삭제
            n = 2*i
            while n < num:
                prime[n] = False
                n += i
    return prime

def search_ans(num, start):
    val = prime[start] + prime[num-start]

    while start <= num-start:
        if prime[start] and prime[num-start]: # start, num-start 모두 소수인 경우
            print(f'{num} = {start} + {num-start}')
            return
        else:
            start += 2

    print("Goldbach's conjecture is wrong.")
    return

nums = []
while True:
    num = int(read().strip())
    if num != 0:
        nums.append(num)
    else: break

prime = prime_seq(max(nums))
for num in nums:
    search_ans(num, 3)