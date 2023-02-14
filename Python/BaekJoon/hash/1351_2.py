# 1351번 무한 수열
# https://www.acmicpc.net/problem/1351

def search_seq(num, p, q):
    if seq.get(num) != None: # dict에 이미 존재하는 경우
        return seq[num]
    else: # 존재하지 않는 경우
        seq[num] = search_seq(num//p, p, q) + search_seq(num//q, p, q)
        return seq[num]

N, P, Q = map(int, input().split())
seq = {0:1, 1:2}
search_seq(N,P,Q)
print(seq[N])