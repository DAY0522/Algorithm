def power(a, b, c):
    if b==1: return a%c
    val = power(a, b//2, c)
    val = (val*val)%c
    if b%2==0: return val
    else: return (val*a)%c

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(power(A,B,C))