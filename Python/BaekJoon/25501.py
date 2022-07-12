# 25501번 재귀의 귀재
# https://www.acmicpc.net/problem/25501

import sys
read = sys.stdin.readline

def recursion(str, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif str[l] != str[r]:
        return 0
    else:
        return recursion(str, l+1, r-1)

def isPalindrome(str):
    return recursion(str, 0, len(str)-1)

for _ in range(int(input())):
    cnt = 0
    str = read().strip()
    # readline은 \n도 받으므로 완전한 문자열로 변환하기 위해선 공백문자를 제거하기 위한 rstrip()을 사용해야 함.
    print(isPalindrome(str), cnt)