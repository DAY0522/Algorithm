from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dec = deque([i for i in range(1, N+1)])
answ = []

while dec:
    for i in range(K-1):
        dec.append(dec.popleft())
    answ.append(dec.popleft())
print("<", end='')
for i in range(len(answ)-1):
    print("%d, "%answ[i], end='')
print(answ[-1], end='')
print(">")