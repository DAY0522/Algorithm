import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    floor = int(input())
    number = int(input())
    peop = list(i for i in range(1, number+1))
    sum = 0
    for _ in range(floor):
        for n in range(1, number):
            peop[n] += peop[n-1]
    print(peop[-1])