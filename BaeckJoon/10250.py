import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split()) # height, width, num
    floor = N % H if not N % H == 0 else H
    num = (N-1) // H + 1
    print(floor*100+num)