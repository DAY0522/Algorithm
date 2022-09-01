def InitNext(p:str): # Next list 생성
    global next
    M = len(p)
    i, j = 0, -1 # i, j 초기화
    while i < M:
        next[i] = next[j] if p[i] == p[j] else j # 개선된 코드(p[i]와 p[j]가 동일하면 next[j]를 넣음)
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

def KMP(p:str, t:str): # p: 찾으려는 값, t: text
    M, N = len(p), len(t)
    InitNext(p)
    i, j = 0, 0
    while i < N:
        if j == M:
            pos.append(i-M+1)
            j = 0
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        i += 1
        j += 1
    if j == M:
        pos.append(i - M + 1)

if __name__ == '__main__':
    text = input()
    pattern = input()

    next = [-1] * len(pattern) # pattern의 크기와 동일한 next 배열 선언
    pos = list() # 찾은 pattern의 위치를 저장할 배열
    KMP(pattern, text) # text에서의 pattern의 위치를 pos 변수에 저장

    print(len(pos))
    for p in pos:
        print(p, end=' ')