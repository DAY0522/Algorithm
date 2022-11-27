def Z_visit(n, r, c):
    global ans

    if not (r <= R < r + n and c <= C < c + n):
        ans += n * n
        return 0

    if R == r and C == c:
        print(ans)
        exit()

    if n == 1:
        ans += 1
        return 0

    Z_visit(n // 2, r, c)
    Z_visit(n // 2, r, c + n // 2)
    Z_visit(n // 2, r + n // 2, c)
    Z_visit(n // 2, r + n // 2, c + n // 2)


if __name__ == '__main__':
    N, R, C = map(int, input().split())
    ans = 0
    Z_visit(2 ** N, 0, 0)