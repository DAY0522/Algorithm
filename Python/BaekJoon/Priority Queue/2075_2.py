# 2075번 N번째 큰 수
# https://www.acmicpc.net/problem/2075
import heapq
import sys
read = sys.stdin.readline

N = int(read().strip())
heap = list(map(int, read().split()))
for _ in range(N-1):
    sub = list(map(int, read().split()))
    for s in sub:
        if s < heap[0]:
            continue
        heapq.heappush(heap, s)
        heapq.heappop(heap)
print(heap[0])