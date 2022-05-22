N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort() # 입력된 수를 정렬

en = 0 # 뒷 포인터
min_val = float('inf') # 큰값을 넣어줌
for st in range(N): # 앞 포인터
    while en < N and nums[en]-nums[st] < M:
    # en과 st에 있는 수의 차가 M보다 크면 이후는 계속 M보다 크므로 경계값까지만 구함
        en += 1
    if en == N: # 인덱스 에러에 대한 예외 처리
        break
    min_val = min(min_val, nums[en]-nums[st]) # 기존 min값과 새로운 값 사이의 최솟값을 구함
print(min_val)