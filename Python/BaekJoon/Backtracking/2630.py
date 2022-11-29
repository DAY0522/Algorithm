import sys

read = sys.stdin.readline


def paper(N, x, y):
    global cnt

    same = True
    for i in range(N):
        for j in range(N):
            if graph[x][y] != graph[x + i][y + j]:
                same = False
                break
        if not same:
            break

    if same:
        cnt[graph[x][y]] += 1
        return 0

    N //= 2
    for i in range(2):
        for j in range(2):
            paper(N, x + N * i, y + N * j)


if __name__ == '__main__':
    N = int(read().strip())
    graph = [list(map(int, read().split())) for _ in range(N)]
    cnt = {0: 0, 1: 0}
    paper(N, 0, 0)
    print(cnt[0])
    print(cnt[1])