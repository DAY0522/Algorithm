import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_A = {input().strip() for _ in range(N)}
set_B = {input().strip() for _ in range(M)}

intersection = list(set_A & set_B)
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)