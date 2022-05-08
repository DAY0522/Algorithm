import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split(' '))
coins = [int(input().strip()) for _ in range(N)]
coins.reverse()
cnt = 0
for c in coins:
    if c <= K:
        cnt += K // c # K를 c로 나눈 몫
        K %= c # K를 c로 나눈 나머지
        if K == 0:
            break
print(cnt)