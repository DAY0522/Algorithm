# 두 수의 합

# 수열을 저장한 리스트를 정렬한다.
# 시작점(st)과 끝점(en)을 지정한다.
# st와 en에서의 값의 합을 sum이라 하자.
# 만약 sum이 x보다 작으면 st에 있는 값을 키워야 한다. 즉 st를 1 더해야 한다.
# 그게 아니라, sum이 x보다 크면 en에 있는 값을 줄여야 한다. 즉 en을 1 빼야 한다.
# 만약 동일하면 cnt를 증가시키고 다음 인덱스에서 탐색한다. (st를 1 증가, en을 1 감소 시킨다.)

n = int(input()) # 수의 개수
nums = list(map(int, input().split()))
x = int(input()) # 두 원소의 합

nums.sort()
cnt = 0 # 개수
st = 0 # 시작점
en = n-1 # 끝점
while st < en:
    sum = nums[st]+nums[en]
    if sum == x:
        cnt += 1
        st += 1
        en -= 1
    elif sum < x:
        st += 1
    else:
        en -= 1
print(cnt)


'''
# 시간 초과
n = int(input()) # 수의 개수
nums = list(map(int, input().split()))
x = int(input()) # 두 원소의 합

nums.sort()
cnt = 0
en = 0
for st in range(n):
    en = st+1
    while en < n and nums[st]+nums[en] < x:
        en += 1
        if en < n and nums[st] + nums[en] == x:
            cnt += 1
            break
print(cnt)
'''