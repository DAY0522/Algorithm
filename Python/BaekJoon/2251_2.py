from collections import deque
A, B, C = map(int, input().split())
visit = [[False]*(B+1) for _ in range(A+1)]
ans = []
que = deque()

# bfs로 풀이
def check_visit(x, y): # x, y를 방문했는지 확인
    if not visit[x][y]:
        que.append((x, y))
        visit[x][y] = True

def bfs(x, y):
    que.append((x, y)) # 시작점
    visit[x][y] = True

    while que:
        x, y = que.popleft()
        z = C - x - y
        if x == 0:
            ans.append(z)

        # A > B로 옮김
        sub = min(x, B-y)
        check_visit(x-sub, y+sub)

        # A > C로 옮김
        sub = min(x, C-z)
        check_visit(x-sub, y)

        # B > A로 옮김
        sub = min(y, A-x)
        check_visit(x+sub, y-sub)

        # B > C로 옮김
        sub = min(y, C-z)
        check_visit(x, y-sub)

        # C > A로 옮김
        sub = min(z, A-x)
        check_visit(x+sub, y)

        # C > B로 옮김
        sub = min(z, B-y)
        check_visit(x, y+sub)

bfs(0, 0)
print(*sorted(ans))