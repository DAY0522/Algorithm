# 2504번 괄호의 값
# https://www.acmicpc.net/problem/2504

from collections import deque

words = input() # 입력
mul = 1 # 곱해줘야 하는 값
stack = deque()

ans = 0 # 결과
for i in range(len(words)):
    if words[i] == '(':
        stack.append('(')
        mul *= 2
    elif words[i] == '[':
        stack.append('[')
        mul *= 3
    elif words[i] == ')':
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
            if words[i-1] == '(':
                ans += mul
            mul //= 2
        else:
            print(0)
            exit()
    elif words[i] == ']':
        if len(stack) != 0 and stack[-1] == '[':
            stack.pop()
            if words[i-1] == '[':
                ans += mul
            mul //= 3
        else:
            print(0)
            exit()

if stack:
    print(0)
else:
    print(ans)