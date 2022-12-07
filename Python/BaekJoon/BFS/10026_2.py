# 10026번 적록색약
# https://www.acmicpc.net/problem/10026

# 나 혼자 풀이한 코드.
# 10026에서는 더 효율적으로 푸는 방법이 없는지 구글링을 하다가 발견하여 재풀이한 방식.
import sys
from collections import deque
read = sys.stdin.readline

que = deque()
pict = [read().strip() for _ in range(int(input()))]
R, C = len(pict), len(pict[0])
visit = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = [0,0]

# r
for row in range(len(pict)):
    for col in range(len(pict[0])):
        if pict[row][col] == 'R' and not visit[row][col]:
            que.append((row, col))
            ans[0] += 1
        while que:
            p_x, p_y = que.popleft()
            visit[p_x][p_y] = 1
            for i in range(4):
                x = p_x + dx[i]
                y = p_y + dy[i]
                if x>=0 and x<R and y>=0 and y<C and not visit[x][y] and pict[x][y]=='R':
                    que.append((x,y))
                    visit[x][y] = 1

# g
for row in range(len(pict)):
    for col in range(len(pict[0])):
        if pict[row][col] == 'G' and not visit[row][col]:
            que.append((row, col))
            ans[0] += 1
        while que:
            p_x, p_y = que.popleft()
            visit[p_x][p_y] = 1
            for i in range(4):
                x = p_x + dx[i]
                y = p_y + dy[i]
                if x>=0 and x<R and y>=0 and y<C and not visit[x][y] and pict[x][y]=='G':
                    que.append((x,y))
                    visit[x][y] = 1

# b
for row in range(len(pict)):
    for col in range(len(pict[0])):
        if pict[row][col] == 'B' and not visit[row][col]:
            que.append((row, col))
            ans[0] += 1
            ans[1] += 1
        while que:
            p_x, p_y = que.popleft()
            visit[p_x][p_y] = 1
            for i in range(4):
                x = p_x + dx[i]
                y = p_y + dy[i]
                if x>=0 and x<R and y>=0 and y<C and not visit[x][y] and pict[x][y]=='B':
                    que.append((x,y))
                    visit[x][y] = 1

visit = [[0 for _ in range(C)] for _ in range(R)]
# r, g
for row in range(len(pict)):
    for col in range(len(pict[0])):
        if pict[row][col] != 'B' and not visit[row][col]:
            que.append((row, col))
            ans[1] += 1
        while que:
            p_x, p_y = que.popleft()
            visit[p_x][p_y] = 1
            for i in range(4):
                x = p_x + dx[i]
                y = p_y + dy[i]
                if x>=0 and x<R and y>=0 and y<C and not visit[x][y] and pict[x][y] != 'B':
                    que.append((x,y))
                    visit[x][y] = 1
print(*ans)