# 1431번 시리얼 번호
# https://www.acmicpc.net/problem/1431
import sys
read = sys.stdin.readline

def sum_digit(str):
    ans = 0
    for s in str:
        if s.isdigit():
            ans += int(s)
    return ans

num = [read().strip() for _ in range(int(read().strip()))]
for n in sorted(num, key=lambda x:(len(x), sum_digit(x), x)):
    print(n)