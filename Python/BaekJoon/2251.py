A, B, C = map(int, input().split())
find = {}
ans = []

# dfs, backtracking으로 풀이
def dfs(a, b, c):
    global A, B, C
    seq = str(a) + '-' + str(b)
    if find.get(seq) != None:  # 이미 존재하는 경우
        return
    else: # 존재하지 않는 경우
        if a==0:
            ans.append(c)
        find[seq] = True

    if a != 0:  # A에 물이 있는 경우
        # A > B
        if a + b > B:
            dfs(a + b - B, B, c)
        else:
            dfs(0, a + b, c)

        # A > C
        if a + c > C:
            dfs(a + c - C, b, C)
        else:
            dfs(0, b, a + c)

    if b != 0:  # B에 물이 있는 경우
        # B > A
        if a + b > A:
            dfs(A, a + b - A, c)
        else:
            dfs(a + b, 0, c)

        # B > C
        if b + c > C:
            dfs(a, b + c - C, C)
        else:
            dfs(a, 0, b + c)

    if c != 0:  # C에 물이 있는 경우
        # C > A
        if c + a > A:
            dfs(A, b, c + a - A)
        else:
            dfs(a + c, b, 0)

        # C > B
        if c + b > B:
            dfs(a, B, c + b - B)
        else:
            dfs(a, b + c, 0)

dfs(0, 0, C)
print(*sorted(ans))