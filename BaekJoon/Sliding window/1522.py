s = input() # 문자열 입력
a = s.count('a') # 입력된 str에서의 a의 개수

s += s[0:a-1] # 원형 문자열
min_val = float('inf') # 최솟값
for i in range(len(s)-(a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)

'''
지원님 코드
from collections import Counter

def solution():
    st = input()
    length = len(st)
    most_char, most_length = Counter(st).most_common(1)[0]
    mini = most_length - Counter(st[:most_length])[most_char]

    st *= 2

    count = mini
    for i in range(1, length):
        if st[i - 1] == most_char:
            count += 1
        else:
            count -= 1

        if st[i + most_length - 1] == most_char:
            count -= 1
        else:
            count += 1

        mini = min(mini, count)

    print(mini)


if __name__ == "__main__":
    solution()
'''