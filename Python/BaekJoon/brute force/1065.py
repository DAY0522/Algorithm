def get_hansu(N):
    if N < 100:
        hansu = N
    else:
        hansu = 99
        for num in range(100, N+1):
            num = list(map(int, str(num)))
            for i in range(1, len(num)-1):
                if num[0]-num[1] == num[1]-num[2]:
                    hansu += 1
    return hansu

print(get_hansu(int(input())))