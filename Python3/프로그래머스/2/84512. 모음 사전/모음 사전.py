def solution(word):
    backTracking('', word)
    return n[1]


## backtracking?
aeiou = ['A', 'E', 'I', 'O', 'U']
n = [0, 0]
def backTracking(w, word):
    # print(n[0], w, word)
    if w == word:
        n[1] = n[0]
        return
    
    if len(w) >= 5:
        return
    
    for i in range(5):
        n[0] += 1
        backTracking(w+aeiou[i], word)
        