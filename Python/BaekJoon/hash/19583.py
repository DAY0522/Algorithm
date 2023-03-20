# 19583번 싸이버개강총회
# https://www.acmicpc.net/problem/19583
import sys
read = sys.stdin.readline
S, E, Q = read().split()
# 시작 / 끝 / 스트리밍 끝

stud = {}
partcipants = set()
while True:
    try:
        time, s = read().split()
        if time <= S:
            stud[s] = time
        elif E <= time <= Q:
            if stud.get(s) != None:
                partcipants.add(s)
        elif time > Q:
            break
    except:
        break
print(len(partcipants))