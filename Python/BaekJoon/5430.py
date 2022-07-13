# 5430번 AC
# https://www.acmicpc.net/problem/5430
from collections import deque
import sys

read = sys.stdin.readline

for _ in range(int(input())):
    ans = False # 결과 출력 여부
    func = input()
    size = int(input())
    arr = deque(input()[1:-1].split(','))

    reverse = False # 뒤집혔는지 여부. R 여부
    left = 0
    right = size # 마지막 원소의 한 칸 뒤

    if not size:
        if set(func.strip()) == {'R'}:
            print('[]')
        else:
            print("error")
        continue

    if not ans:
        for f in func:
            if f == 'R': # 뒤집어 줌
                reverse = not reverse
            else: # D인 경우
                if reverse:  # 뒤집힌 경우
                    right -= 1
                else:
                    left += 1

                if not left <= right:
                    print("error")
                    ans = True
                    break

    if not ans:
        print('[', end='')
        if reverse:
            for i in range(right-1, left, -1):
                print(arr[i], end=',')
            end = left
        else:
            for i in range(left, right-1):
                print(arr[i], end=',')
            end = right-1
        if left < right:
            print(arr[end] + ']')
        else:
            print(']')