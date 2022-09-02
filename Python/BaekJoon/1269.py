# 1269번 대칭 차집합
# https://www.acmicpc.net/problem/1269


input()
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

print(len((set_A-set_B)|(set_B-set_A)))