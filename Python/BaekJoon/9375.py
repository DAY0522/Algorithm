# 9375번 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

import sys
read = sys.stdin.readline

for _ in range(int(input())):
    set_clothes = set()
    dict_clothes = dict()
    for _ in range(int(input())): # 동일한 의상 제거
        set_clothes.add(read().strip())
    for c in set_clothes:
        try:
            dict_clothes[c.split(' ')[1]] += 1
        except:
            dict_clothes[c.split(' ')[1]] = 1

    ans = 1
    for _, value in dict_clothes.items():
        ans *= value+1
    print(ans-1)