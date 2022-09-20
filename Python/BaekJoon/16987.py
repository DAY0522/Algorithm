def dfs(cur): # cur번째 계란으로 다른 계란을 깨는 함수
    global ans, cnt

    if cur==N:
        ans = max(ans, cnt)
        return

    if s[cur]<0 or cnt==N-1: # 이미 깨져있거나, 더 이상 깰 게 없는 경우
        dfs(cur+1)
        return

    for i in range(N):
        if cur!=i and s[i]>0: # 현재 계란이 아니고, 깨려는 계란이 안 깨진 경우
            s[i] -= w[cur]
            s[cur] -= w[i]
            if s[i]<=0: cnt+=1
            if s[cur]<=0: cnt+=1
            dfs(cur+1)
            if s[i]<=0: cnt-=1
            if s[cur]<=0: cnt-=1
            s[i] += w[cur]
            s[cur] += w[i]

N = int(input())
s = [0]*N # 내구성
w = [0]*N # 무게
ans = 0
cnt = 0

for i in range(N):
    s[i], w[i] = map(int, input().split())

dfs(0)
print(ans)