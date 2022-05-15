# 13305 주유소
# 마지막 도시의 주유 비용은 굳이 신경 안 써도 된다.
# 총 길이의 합과 충전 횟수는 동일

# 현재 주유 비용에서 더 작은 주유 비용이 나올 때까지
# 그 사이의 값들은 현재 주유 비용을 통해 계산한다.
N = int(input()) # 도시의 개수
len = list(map(int, input().split())) # 각 도시 사이 거리
cost = list(map(int, input().split())) # 주유소 비용

cur = 0 # 현재 도시의 위치
result = 0 # 최종 주유 비용
for i in range(0, N-1):
    if cost[i] < cost[cur]:
        cur = i
    result += cost[cur]*len[i]
print(result)