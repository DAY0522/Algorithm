# 1002번 터렛
# https://www.acmicpc.net/problem/1002
import sys
read = sys.stdin.readline

# 원래는 두 점 사이의 거리를 구할 때 sqrt()를 사용했는데
# 이렇게 되면 후에 부동소수점에서의 오차로 인해 r3 == r1 + r2와 같이
# 정수와 비교하게 될 때, 오차 때문에 False가 된다고 한다.(==는 완전히 일치하는지만을 확인하므로)
# 그래서 sqrt()를 쓰지 않고 하는 방법을 이용하는 것이 중요하다.
# (근데 여기선 사용해도 채점 되긴 하던데...)
# 아무튼 다른 유사 문제들에서도 주의하자!

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, read().split()) # 각 점 입력
    r3 = (x1-x2)**2 + (y1-y2)**2
    if r3 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r3 == (r1 + r2)**2:
            print(1)
        elif r3 > (r1 + r2)**2:
            print(0)
        elif r3 < (r1 + r2)**2:
            if r3 < abs(r1-r2)**2:
                print(0)
                continue
            elif r3 == abs(r1-r2)**2:
                print(1)
                continue
            print(2)

"""
import sys
import math
read = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, read().split()) # 각 점 입력
    r3 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if r3 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r3 == r1 + r2:
            print(1)
        elif r3 > r1 + r2:
            print(0)
        elif r3 < r1 + r2:
            if r3 + r1 < r2 or r3 + r2 < r1:
                print(0)
                continue
            elif r3 == abs(r1-r2):
                print(1)
                continue
            print(2)
"""