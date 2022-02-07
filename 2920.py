s = list(map(int, input().split()))

if s[0] != 1 and s[0] != 8:
    print("mixed")
elif s[0] == 1:
    for n in range(0,len(s)-1):
        if s[n+1] != s[n] + 1:
            print("mixed")
            exit()
    print("ascending")
elif s[0] == 8:
    for n in range(0,len(s)-1):
        if s[n+1] != s[n] - 1:
            print("mixed")
            exit()
    print("descending")