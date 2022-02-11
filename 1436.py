N = int(input())
count = 0
i = 665

while(1):
    result = str(i).find("666")
    if result >= 0:
        count += 1
    if N == count:
        print(i)
        exit()
    i += 1