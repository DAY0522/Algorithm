# 1822번 차집합
# https://www.acmicpc.net/problem/1822

def binary_search(num):
    start = 0
    end = len(B_list)-1

    while start <= end:
        mid = (start+end)//2
        if num < B_list[mid]: # num이 더 작은 경우
            end = mid - 1
        elif num > B_list[mid]: # num이 더 큰 경우
            start = mid + 1
        else: # 같은 경우
            return True
    return False


A, B = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
B_list.sort()

cnt = 0
ans = []
for a in A_list:
    if not binary_search(a): # a가 B_list에 있지 않은 경우
        cnt += 1
        ans.append(a)

ans.sort()
if cnt:
    print(cnt)
    print(*ans)
else:
    print(0)