# 1799번 비숍
# https://www.acmicpc.net/problem/1799

# 구간을 나눠서 구한다음에 각 구간별 횟수를 더해줄 생각을 어떻게 하지?

import sys
read = sys.stdin.readline
N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]
visited_1 = [False] * (2*N-1) # 우하향
visited_2 = [False] * (2*N-1) # 우상향

ans = 0
def dfs(cnt, r, c): # cur은 현재 우상향 대각선 위치
    global ans

    if c>N-1:
        r += 1
        if c%2==0:  c=1
        else: c=0

    if r>N-1:
        ans = max(ans, cnt)
        return

    if graph[r][c] and not visited_1[r+c] and not visited_2[r-c+N-1]:
        # r, c 자리에 놓는 경우
        graph[r][c] = 0
        visited_1[r+c] = True
        visited_2[r-c+N-1] = True
        dfs(cnt+1, r, c+2)
        visited_2[r-c+N-1] = False
        visited_1[r + c] = False
        graph[r][c] = 1

    # r, c 자리에 안 놓는 경우
    dfs(cnt, r, c + 2)

dfs(0, 0, 0)
dfs(ans, 0, 1)

print(ans)