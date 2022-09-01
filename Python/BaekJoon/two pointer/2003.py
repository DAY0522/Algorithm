# 2003번 수들의 합 2

# N : 배열 크기
# M : 합의 크기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 조건에 따라 포인터를 바꿔가며 연산량을 줄임
cnt = 0
st, en = 0, 1
val = A[st]
while st < N:
    # 인덱스 넘은 경우 예외 처리
    if val == M:
        cnt += 1
        val -= A[st]
        st += 1

    if en == N and val < M:
        break
    elif val < M:
        val += A[en]
        en += 1
    elif val > M:
        val -= A[st]
        st += 1

print(cnt)

'''
# 시간초과
# 동일한 부분에 대해 연산이 반복되기 때문에 비효율적
N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for st in range(N):
    for en in range(st + 1, st + (M + 1)):
        if sum(A[st:en]) >= M:
            break
    if sum(A[st:en]) == M:
        cnt += 1
print(cnt)
'''