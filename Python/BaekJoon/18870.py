import sys
input = sys.stdin.readline

N = int(input())
coordinate = list(map(int, input().split()))
s_coordinate = sorted(set(coordinate))
d_coordinate = {s_coordinate[i]:i for i in range(len(s_coordinate))}

for c in coordinate:
    print(d_coordinate[c], end=' ')