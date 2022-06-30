# 11501번 주식
# https://www.acmicpc.net/problem/11501
import sys
read = sys.stdin.readline

for _ in range(int(read().strip())):
    N = int(read().strip())
    money = list(map(int, read().split()))[::-1]
    M_money = 0 # Max 값
    ans = 0
    for i in range(len(money)):
        if M_money < money[i]:
            M_money = money[i]
            continue
        ans += M_money-money[i]
    print(ans)