# 1004번 어린 왕자
# https://www.acmicpc.net/status?from_mine=1&problem_id=1004&user_id=12201856&language_id=1003

def isInside(circle, pos):
    if (circle[0]-pos[0])**2 + (circle[1]-pos[1])**2 < circle[2]**2:
        return True
    return False

for _ in range(int(input())):
    pos = list(map(int, input().split()))

    cnt = 0
    for _ in range(int(input())):
        circle = list(map(int, input().split()))
        if isInside(circle, pos[0:2]) != isInside(circle, pos[2:]):
            cnt += 1
    print(cnt)