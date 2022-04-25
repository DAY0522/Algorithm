# hash 이용
def solution(participant, completion):
    hashComp = {}
    sumHash = 0
    for part in participant:
        hashComp[hash(part)] = part;
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashComp[sumHash]