# 수학적으로 접근
import math
N = int(input()) # 굴다리 길이
M = int(input()) # 가로등 개수
pos = list(map(int, input().split()))

val = [pos[0], N-pos[-1]] # 처음과 끝의 거리 저장
for i in range(1, len(pos)):
    val.append(math.ceil((pos[i]-pos[i-1])/2))
print(max(val))