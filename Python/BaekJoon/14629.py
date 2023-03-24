# 14629번 숫자 조각
# https://www.acmicpc.net/problem/14629

N = input().strip() # str
num_large = ''
num_small = ''

if int(N)>=9876543210:
    print(9876543210)
    exit()

# 작은 수 찾기
visit = [False] * 10
flag = 0
while flag < len(N):
    num = int(N[flag])
    if not visit[num]:
        num_small += str(num)
        flag += 1
        visit[num] = True
    else:
        for i in range(num-1, -1, -1):
            if not visit[i]:
                num_small += str(i)
                visit[i] = True
                for rem in range(9, -1, -1):
                    if not visit[rem]:
                        num_small += str(rem)
                num_small = num_small[:len(N)]
                flag = len(N)
                break
        while flag != len(N):
            flag -= 1
            prev = int(num_small[flag])
            num_small = num_small[:flag]
            visit[prev] = False
            for i in range(prev-1, -1, -1):
                if not visit[i]:
                    num_small += str(i)
                    visit[i] = True
                    for rem in range(9, -1, -1):
                        if not visit[rem]:
                            num_small += str(rem)
                    num_small = num_small[:len(N)]
                    flag = len(N)
                    break

# 큰 수 찾기
visit = [False] * 10
flag = 0
while flag < len(N):
    num = int(N[flag])
    if not visit[num]:
        num_large += str(num)
        flag += 1
        visit[num] = True
    else:
        for i in range(num+1, 10):
            if not visit[i]:
                num_large += str(i)
                visit[i] = True
                for rem in range(10):
                    if not visit[rem]:
                        num_large += str(rem)
                num_large = num_large[:len(N)]
                flag = len(N)
                break
        while flag != len(N):
            flag -= 1
            prev = int(num_large[flag])
            num_large = num_large[:flag]
            visit[prev] = False
            for i in range(prev+1, 10):
                if not visit[i]:
                    num_large += str(i)
                    visit[i] = True
                    for rem in range(10):
                        if not visit[rem]:
                            num_large += str(rem)
                    num_large = num_large[:len(N)]
                    flag = len(N)
                    break

if int(N)-int(num_small) <= int(num_large)-int(N):
    print(int(num_small))
else: print(int(num_large))