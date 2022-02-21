import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    pos = deque([0 for _ in range(N)])
    pos[M] = 1
    queue = deque(map(int, input().split()))

    count = 1
    while True:
        if queue[0] == max(queue):
            queue.popleft()
            if pos.popleft() == 1:
                print(count)
                break
            count += 1
        else:
            queue.append(queue.popleft())
            pos.append(pos.popleft())
