# 3036번 링
# https://www.acmicpc.net/problem/3036

import fractions

N = int(input())
ring = list(map(int, input().split()))

ans = fractions.Fraction(1, 1)
for i in range(N-1):
    ans = ans * fractions.Fraction(ring[i], ring[i+1])
    print(f"{ans.numerator}/{ans.denominator}")