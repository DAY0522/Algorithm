# 11051번 이항 계수 2
# https://www.acmicpc.net/problem/11051

# Method 1
N, K = map(int, input().split())
K_min = min(K, N-K)

numerator, denominator = 1, 1 # 분자, 분모

for i in range(K):
    numerator *= N - i
    denominator *= i + 1
print((numerator//denominator) % 10007)
# int(numerator/denominator)와 같이 하면 부동 소수점의 한계로 정확한 값이 아닌 근사값이 도출됨.
# 따라서 / 연산에 유의해야 함.