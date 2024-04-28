def solution(m, n, puddles):
    answer = 0
    
    INF = float('inf')
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    
    for i in range(1, n+1): # 행
        for j in range(1, m+1): # 열
            if i==1 and j==1: continue
            if [j, i] in puddles: # 물 웅덩이인 경우 넘어가기
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
    
    return dp[i][j]