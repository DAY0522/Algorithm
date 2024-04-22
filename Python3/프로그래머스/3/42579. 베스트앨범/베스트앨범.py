def solution(genres, plays):
    answer = []
    
    infos = {}
    for i in range(len(genres)):
        genre = genres[i]
        if infos.get(genre): # genre가 존재하는 경우
            infos[genre][0] += plays[i]
            infos[genre][1].append((plays[i], i)) # play와 index 삽입
        else: # genre가 존재하지 않는 경우
            infos[genre] = [plays[i], [(plays[i], i)]]
    
    infos = dict(sorted(infos.items(), key = lambda x:x[1][0], reverse=True))
    for k, v in infos.items():
        play = v[1]
        print(play)
        play.sort(key = lambda x:x[1])
        play.sort(key = lambda x:x[0], reverse=True)
        print(play)
        length = 2 if len(play)>=2 else len(play)
        for i in range(length):
            answer.append(play[i][1])
            
    return answer