word_set = {input() for i in range(int(input()))}
word_list = list(word_set)
word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)