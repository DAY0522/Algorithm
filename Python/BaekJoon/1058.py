# 1058번 친구
# https://www.acmicpc.net/problem/1058
import sys
import copy
read = sys.stdin.readline

N = int(read().strip())
graph = [list(read().strip()) for _ in range(N)]

ans = 0
for n in range(N):
    cnt = 0
    stu = copy.deepcopy(graph[n])
    for cur in range(N): # 현재 학생
        if graph[n][cur] == 'Y':

            for next in range(N): # 2-친구 찾기
                if graph[cur][next] == 'Y':
                    stu[next] = 'Y'

    cnt += stu.count('Y')
    if stu[n] == 'Y': cnt -= 1
    ans = max(cnt, ans)
print(ans)