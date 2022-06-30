# 11501번 주식
# https://www.acmicpc.net/problem/11501
import sys
read = sys.stdin.readline

for _ in range(int(read().strip())):
    N = int(read().strip())
    money = [0]+list(map(int, read().split()))

    if len(set(money))==2:
        print(0)
        continue
    ans = 0
    max_m = max(money)
    st = 1
    while st<len(money):
        if money[st]==max_m:
            ans += max_m*(st-1)-sum(money[1:st])
            money = [0]+money[st+1:]
            st = 0
            if len(money)<=1: break
            max_m = max(money)
        st = st + 1
    print(ans)