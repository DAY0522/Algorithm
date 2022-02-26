import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
dec = deque([i for i in range(1, n+1)])
result = deque()

for i in num:
    result.append()