from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
dec = deque()
for _ in range(K):
    num = int(input())
    if num != 0:
        dec.append(num)
    else:
        dec.pop()
print(sum(dec))