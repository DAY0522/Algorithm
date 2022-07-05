K = int(input())
length = []
dirc = []
result = [False, False, False, False]
big, small = 1, 1

for _ in range(6):
    dir, len = map(int, input().split())
    length.append(len)
    dirc.append(dir)
max_index = length.index(max(length))

length = length[max_index:] + length[0:max_index]
dirc = dirc[max_index:] + dirc[0:max_index]

for i in range(6):
    if result[dirc[i] - 1]:  # 앞에서 같은 방향이 나온 경우
        small = length[i] * length[i - 1]  # 빼줘야하는 값
        break
    result[dirc[i] - 1] = True

for i in range(1, 4 + 1):
    if dirc.count(i) == 1:
        big *= length[dirc.index(i)]
print(K * (big - small))