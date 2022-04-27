cur = list(map(int, input().split()))
time = int(input())

cur[0] = (cur[0] + (cur[1] + time)//60) % 24
cur[1] = (cur[1] + time) % 60
print(cur[0], cur[1])