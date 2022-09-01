import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().strip().split())) for _ in range(N)]
times.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간을 기준으로 정렬
cnt = end = 0 # 회의 수와 끝나는 시간을 0으로 초기화
for t in times: # 정렬된 회의 시간을 순회
    if t[0] >= end: # 이전 회의의 끝 시간(end)보다 시작 시간이 크면 조건 만족
        cnt += 1
        end = t[1] # 끝 시간 갱신
print(cnt)