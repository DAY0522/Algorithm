import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    cnt_zero = [1, 0]
    cnt_one = [0, 1]
    N = int(input())

    for n in range(N):
        cnt_zero.append(cnt_one[-1])
        cnt_one.append(cnt_one[-2] + cnt_one[-1])
    print(cnt_zero[N], cnt_one[N])