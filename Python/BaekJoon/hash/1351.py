# 1351번 무한 수열
# https://www.acmicpc.net/problem/1351

# 시간 초과 발생
from collections import deque
N, P, Q = map(int, input().split())

if N==0:
    print(1)
    exit()

if P > Q: # P에 더 작은 값 저장
    P, Q = Q, P

cnt = 0 # 삭제된 원소의 개수
seq = deque([1,2])
N_max = max(N//P, N//Q)
for i in range(2, N_max+1):
    if i % Q == 0: # 나누어 떨어질 경우
        seq.popleft()
        cnt += 1
    # print(i//P-cnt, i//Q-cnt, cnt)
    # print(seq[i//P-cnt], seq[i//Q-cnt])
    seq.append(seq[i//P-cnt] + seq[i//Q-cnt])
print(seq[N//P-cnt] + seq[N//Q-cnt])