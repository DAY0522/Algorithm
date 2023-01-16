# 2910번 빈도 정렬
# https://www.acmicpc.net/problem/2910
N, K = map(int, input().split())
arr = list(map(int, input().split()))
freq = {}
for a in arr:
    try:
        freq[a] += 1
    except:
        freq[a] = 1
# sorted(freq.items(), key=lambda x:x[1], reverse=True)와 같이 풀이 가능
arr.sort(key=lambda x:(N-freq[x], list(freq).index(x)))
print(*arr)

