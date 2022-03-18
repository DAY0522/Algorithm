import sys
input = sys.stdin.readline

height = [int(input().strip()) for _ in range(9)]
sub = sum(height) - 100

for i in range(9):
    for j in range(9):
        if i==j: break
        if height[i]+height[j]==sub:
            height.pop(i)
            height.pop(j)
            for i in sorted(height):
                print(i)
            exit()