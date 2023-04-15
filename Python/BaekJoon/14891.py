# 14891번 톱니바퀴
# https://www.acmicpc.net/problem/14891
import sys
read = sys.stdin.readline

def rotate_gear(i, type): # 기어 회전해주는 함수
    if type == 1: # 시계 방향 회전
        gear[i] = gear[i][-1:] + gear[i][:-1]
    else: # 반시계 방향 회전
        gear[i] = gear[i][1:] + gear[i][:1]

def same_gear(): # 맞닿은 부분의 극이 같은지 확인하는 함수
    same = []

    if gear[1][2] == gear[2][6]: # 같은 극
        same.append(True)
    else:
        same.append(False)

    if gear[2][2] == gear[3][6]: # 같은 극
        same.append(True)
    else:
        same.append(False)

    if gear[3][2] == gear[4][6]:  # 같은 극
        same.append(True)
    else:
        same.append(False)
    return same


gear = ['']
for _ in range(4):
    gear.append(list(map(int, read().strip())))

K = int(read().strip())
for _ in range(K):
    num, type = map(int, read().split())
    same = same_gear()

    rotate_gear(num, type)  # 방향대로 돌리기
    if num == 1: # 1번 톱니바퀴를 돌리는 경우
        for i in range(3):
            if same[i]: break # 극이 같을 시 바로 종료

            # 방향이 다른 경우
            type = -type # 방향 변경
            rotate_gear(i+2, type)

    elif num == 2: # 2번 톱니바퀴를 돌리는 경우
        if not same[0]: # 1-2 맞닿은 게 서로 다를 시
            rotate_gear(1, -type)

        for i in range(1, 3):
            if same[i]: break # 극이 같을 시 바로 종료

            # 방향이 다른 경우
            type = -type # 방향 변경
            rotate_gear(i+2, type)

    elif num == 3: # 3번 톱니바퀴를 돌리는 경우
        if not same[2]: # 3-4 맞닿은 게 서로 다를 시
            rotate_gear(4, -type)

        for i in range(1, -1, -1):
            if same[i]: break # 극이 같을 시 바로 종료

            # 방향이 다른 경우
            type = -type # 방향 변경
            rotate_gear(i+1, type)

    else: # 4번 톱니바퀴
        for i in range(2, -1, -1):
            if same[i]: break # 극이 같을 시 바로 종료

            # 방향이 다른 경우
            type = -type # 방향 변경
            rotate_gear(i+1, type)

ans = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        ans += 2**(i-1)
print(ans)