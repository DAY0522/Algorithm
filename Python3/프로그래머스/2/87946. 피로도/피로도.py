# 최소 필요 피로도 / 소모피로도
# [[10,10],[50,40],[30,10]]
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    per = list(permutations(dungeons))
    for i in range(len(per)):
        cur = [0, k] # 탐험한 횟수, 피로도
        for x, y in per[i]:
            if cur[1] >= x:
                cur[1] -= y
                cur[0] += 1
        answer = max(cur[0], answer)
        if answer == len(per):
            return answer
    
    return answer