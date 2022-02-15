p = input()

count = len(list(map(int, str(p)))) # 자리수

min = int(p) - 9 * count
if min <= 0 : min = 1

for i in range(min, int(p)):
    m = i + sum(list(map(int, str(i))))

    if(int(p)==m):
        print(i)
        exit()
print(0)