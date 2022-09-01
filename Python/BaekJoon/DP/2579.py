import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 계단 개수
s = deque([int(input().strip()) for _ in range(N)])
s.appendleft(0) # 인덱스 맞추기 위해 0 추가
res = [0] * (N+1) # 출력 결과

if N == 1: # N이 1일 때 런타임 에러 방지
    print(s[1])
else:
    # 1, 2일 때는 예외
    res[1] = s[1]
    res[2] = s[2] + s[1]

    # i층에 오를 때,
    # i의 전 층에서 올라오는 경우
    # i의 전전 층에서 올라오는 경우 존재
    for i in range(3, N+1):
        res[i] = max(s[i] + s[i-1] + res[i-3], s[i] + res[i-2])

    print(res[N])