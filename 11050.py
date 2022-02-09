def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)

N, K = map(int, input().split())

print(int((factorial(N)/factorial(N-K))/factorial(K)))