# 1309번 동물원
# https://www.acmicpc.net/problem/1309

N = int(input())
prev = [1, 2]
next = [1, 2]
for _ in range(2, N+1):
    next[0] = prev[0] + prev[1]
    next[1] = prev[0]*2 + prev[1]
    prev[0], prev[1] = next[0]%9901, next[1]%9901
print((prev[0]+prev[1])%9901)