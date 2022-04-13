# Code1
word = input()
words = list()

for i in range(0, len(word)-2):
    for j in range(i+1, len(word)-1):
        front = word[i::-1] # i번째 부터 시작까지 거꾸로
        mid = word[j:i:-1] # j번째 값부터 i 앞까지 거꾸로
        back = word[:j:-1]
        words.append(front+mid+back)
print(sorted(words)[0])

'''
# Code2
word = list(input())
words = []
result = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        front = word[:i]
        mid = word[i:j]
        back = word[j:]

        front.reverse()
        mid.reverse()
        back.reverse()

        words.append(front+mid+back)

for w in words:
    result.append(''.join(w))

print(sorted(result)[0])
'''