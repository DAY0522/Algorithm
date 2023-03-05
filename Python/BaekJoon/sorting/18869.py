# 18869번 멀티버스2
# https://www.acmicpc.net/problem/18869

# 행성을 1,2,3,4, ... 와 같이 번호 매겨서
# 행성의 크기 대로 숫자를 정렬했을 때
# 숫자 배열이 같으면 균등한 우주이다.

import sys
read = sys.stdin.readline

M, N = map(int, read().split())

result = {}
for _ in range(M):
    cosmos = list(map(int, read().split()))
    cos_sort = sorted(cosmos) # 입력을 정렬
    idx = {cos_sort[i]:i for i in range(N)}
    id = str([idx[c] for c in cosmos])
    result[id] = result.get(id, 0) + 1

cnt = 0
for k, v in result.items():
    cnt += v*(v-1)//2
print(cnt)