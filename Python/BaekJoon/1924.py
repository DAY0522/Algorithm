# 1924번
# https://www.acmicpc.net/status?user_id=12201856&problem_id=1924&from_mine=1
x, y = map(int, input().split())
last = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

day = y
for i in range(x-1):
    day += last[i]

day %= 7
if day==0:
    print("SUN")
elif day==1:
    print("MON")
elif day==2:
    print("TUE")
elif day==3:
    print("WED")
elif day==4:
    print("THU")
elif day==5:
    print("FRI")
elif day==6:
    print("SAT")