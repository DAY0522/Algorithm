# 2457번 공주님의 정원
# https://www.acmicpc.net/problem/2457
import sys
read = sys.stdin.readline
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

arr = []
march, nomem = 60, 334
for _ in range(int(read().strip())):
    m1, d1, m2, d2 = map(int, read().split())
    sum1, sum2 =0, 0
    for i in range(m1-1):
        sum1 += day[i]
    sum1 += d1

    for i in range(m2 - 1):
        sum2 += day[i]
    sum2 += d2
    arr.append([sum1,sum2])
arr.sort(key=lambda x:(x[0], x[1]))

cnt = 0
prev, cur = 0, 0 # 이전 끝/현재 끝 날짜

if len(arr)==1:
    if arr[0][0] <= march and arr[0][1] > nomem: print(1)
    else: print(0)
    exit()

i = 0
for k in range(len(arr)):
    if arr[k][0] <= march:
        prev = arr[k][1]
        cnt = 1
        i = k+1
    else:
        break

if prev == 0:
    print(0)
    exit()

cur = prev

while prev<=nomem and i<len(arr):
    start = arr[i][0]
    end = arr[i][1]
    if start<=prev:
        if cur<end:
            cur = end
        i += 1
    else:
        if prev==cur: # 만족하는 게 없는 경우
            print(0)
            exit()
        prev = cur
        cnt+=1
    if len(arr) and cur == arr[-1][1]:
        cnt += 1
if cur <= nomem:
    print(0)
    exit()


print(cnt)