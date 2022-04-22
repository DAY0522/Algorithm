import sys
input = sys.stdin.readline
num = [int(input().strip()) for _ in range(int(input()))]

print(round(sum(num)/len(num))) #산술평균

sort_num = sorted(num)
print(sort_num[len(sort_num)//2]) #중앙값

freq = {} #빈도수를 dict에 저장
for i in sort_num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
Max_freq = [k for k,v in freq.items() if max(freq.values()) == v]
print(Max_freq[0] if len(Max_freq)==1 else Max_freq[1]) #최빈값

print(sort_num[-1]-sort_num[0]) #범위