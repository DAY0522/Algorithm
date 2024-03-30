def solution(answers):
    answer = []
    
    pick1 = [1,2,3,4,5]
    pick2 = [2,1,2,3,2,4,2,5]
    pick3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [[0, 1], [0, 2], [0, 3]]
    for i in range(len(answers)):
        score[0][0] += 1 if pick1[i%5] == answers[i] else 0
        score[1][0] += 1 if pick2[i%8] == answers[i] else 0
        score[2][0] += 1 if pick3[i%10] == answers[i] else 0
        
    score = sorted(score, key = lambda x:x[0], reverse = True)
    max_num = score[0][0]
    for x, y in score:
        if x == max_num:
            answer.append(y)
    
    return answer