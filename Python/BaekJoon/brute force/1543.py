# 1543번 문서 검색
# https://www.acmicpc.net/problem/1543

all = input() # 문서
match = input() # 단어

# print(all.count(match))

cur = 0 # 현재 확인하고 있는 인덱스
ans = 0 # 결과값

while cur < len(all):
    cnt = 0 # 일치한 단어 수
    if all[cur] == match[0]: # 매치할 문자의 첫 문자열과 동일한 경우
        cnt += 1 # 일치한 단어 수 증가
        for i in range(1, len(match)): # 맨 첫 글자 제외 n-1개의 문자가 같은지 확인
            if cur+i >= len(all) or all[cur+i] != match[i]: # 다음 문자가 같은지 확인
                break # 다른 경우 바로 멈춤
            else: cnt += 1

    cur += 1
    if cnt == len(match): # 모든 것이 일치하는 경우
        # print(cur-1, '다음 cur', cur+len(match))
        ans += 1
        cur = cur - 1 + len(match) # 다음 문서의 인덱스
print(ans)