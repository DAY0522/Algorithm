import sys
from collections import deque
input = sys.stdin.readline
card = deque([i for i in range(1, int(input())+1)])

while len(card)>1:
    card.popleft()
    card.append(card.popleft())
print(card.popleft())