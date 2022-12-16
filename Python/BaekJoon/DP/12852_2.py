# 12852번 1로 만들기 2
# https://www.acmicpc.net/problem/12852

# 해당 코드는 파이썬 코드를 찾아보던 중 deque를 이용해 푼 풀이가 있길래
# 이를 활용해 다시 풀어본 코드이다.

# 그런데 시간초과 난다... 아이디어만 가져가자

from collections import deque

N = int(input())
que = deque()
que.append([N])

while True:
    p = que.popleft()
    x = p[0]
    if x==1:
        print(len(p)-1)
        print(*p[::-1])
        break

    if x%3==0:
        que.append([x//3]+p)

    if x%2==0:
        que.append([x//2]+p)

    que.append([x-1]+p)