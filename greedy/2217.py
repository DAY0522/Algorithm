import sys
input = sys.stdin.readline

N = int(input())
loops = [int(input().strip()) for _ in range(N)]
loops.sort(reverse=True)

weight = 0
loops = [loops[i] * (i+1) for i in range(N)]

"""
case 1
for i in range(N):
    if loops[i] * (i+1) >= weight:
        weight = loops[i] * (i+1)

#    else:
#        break
#        1 1 1 3 넣으면 4인데 else 넣으면 3 나옴. 그니까 끝까지 확인해야 함.

"""
print(max(loops))