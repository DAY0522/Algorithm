# 13915 현수의 열기구 교실
# https://www.acmicpc.net/problem/13915
import sys
read = sys.stdin.readline

while True:
    try:
        N = int(read().strip())
        all = set()
        for i in range(N):
            per = set(sorted(list(read().strip())))
            all.add(str(per))
        print(len(all))
    except:
        exit()