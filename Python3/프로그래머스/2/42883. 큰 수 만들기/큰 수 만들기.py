def solution(number, k):
    answer = ''
    
    N = len(number)
    visit = [False] * N # 사용했는지 여부
    cur = -1
    for i in range(N - k, 0, -1):
        # print(i)
        num = -1
        idx = -1
        for j in range(cur+1, N-i+1):
            # print(f'cur: {cur}, number: {number[j]}')
            if int(number[j]) > num and visit[j] == False:
                num = int(number[j])
                idx = j
                cur = idx
                if num == 9:
                    break
        visit[idx] = True
        answer += str(num)
                
        
    return answer