import sys

M, N = map(int, sys.stdin.readline().split())
board = []
for i in range(M):
    board.append(sys.stdin.readline().strip())

mini = list()
for i in range(M-7):
    for j in range(N-7):
        start_W, start_B = 0, 0 # W와 B로 시작했을 때, 각각 다시 칠해야 할 개수
        for m in range(i, i + 8):
            for n in range(j, j + 8):
                # B로 시작
                if (m+n) % 2 == 0 and board[m][n] != 'B': start_B += 1
                elif (m+n) % 2 == 1 and board[m][n] != 'W': start_B += 1
                    
                # W로 시작
                if (m+n) % 2 == 0 and board[m][n] != 'W': start_W += 1
                elif (m+n) % 2 == 1 and board[m][n] != 'B': start_W += 1

        mini.append(start_B)
        mini.append(start_W)
print(min(mini))