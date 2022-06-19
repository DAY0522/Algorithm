import sys
read = sys.stdin.readline

t = 0
while True:
    ans = 0
    try:
        L, P, V = map(int, read().split())
        t += 1
        add = V%P if V%P<=L else L
        print(f'Case {t}: {L*(V//P) + add}')
    except: break