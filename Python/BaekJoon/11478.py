# 11478번 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

result = set()
str = input()

for i in range(len(str)):
    for j in range(i, len(str)):
        result.add(str[i:j+1])

print(len(result))

"""
result = set()
str = input()

for i in range(1, len(str)+1):
    for j in range(len(str)-i+1):
        result.add(str[j:j+i])

print(len(result))
"""