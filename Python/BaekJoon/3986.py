# 3986번 좋은 단어
# https://www.acmicpc.net/problem/3986

# 괄호쌍이 올바른지 구하는 문제와 동일하게 푸려고 했다.
# A나 B가 짝수번 입력될 때마다 pop을 하려고 했다. > 하지만 짝수개 입력된다고 무조건 짝이 아니다.
# 또 top에 있는 게 append 되려는 것과 일치하지 않아도 된다.
# 위 같은 사실들을 간과해 처음에 오답이 나왔다.

# 입력을 하다가 연달아 문자가 동일한 경우. 즉, top과 append 하려는 값이 동일한 경우만 pop하면 된다.
# 이를 계속 반복했을 때 stack에 남아있는 게 있다면, 좋은 단어가 아닌 것이다.

import sys
from collections import deque
read = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    word = read().strip()
    stack = deque()
    result = True

    if len(word) % 2: # 크기가 홀수인 경우
        continue

    for w in word:
        if len(stack) != 0 and stack[-1] == w: # 크기가 0이 아니고 top과 동일할 때 pop
            stack.pop()
            continue
        stack.append(w) # 동일하지 않은 경우 일단 append

    if not stack:
        ans += 1

print(ans)