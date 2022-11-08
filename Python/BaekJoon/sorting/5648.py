# 5648번 역원소 정렬
# https://www.acmicpc.net/problem/5648
import sys
read = sys.stdin.readline

def sort_str(str):
    return int(str[::-1])

num = read().split()
while len(num)<(int(num[0])+1):
    num += read().split()

for i in range(1, len(num)):
    num[i] = sort_str(num[i])

for n in sorted(num[1:]):
    print(n)