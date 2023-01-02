from collections import deque

def backT(cur, x, y):
    global cnt, Y_cnt

    if cur==7:
        cnt += 1
        return

    if Y_cnt>3: # 4번 조건에 만족하지 못함
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
            if stud[nx][ny]=='Y': Y_cnt+=1
            visited[nx][ny]=True
            backT(cur+1, nx, ny)
            if stud[nx][ny] == 'Y': Y_cnt -= 1
            visited[nx][ny]=False




stud = [input().strip() for _ in range(5)]
visited = [[False]*5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
Y_cnt = 0
for x in range(5):
    for y in range(5):
        visited[x][y] = True
        if stud[x][y]=='Y': Y_cnt+=1
        backT(1, x, y)
        if stud[x][y] == 'Y': Y_cnt -= 1
        visited[x][y] = False
print(cnt//2)