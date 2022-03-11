import sys
input = sys.stdin.readline
L = int(input())
term = input()
sum = 0
for i in range(len(term)-1):
    sum += ((ord(term[i])-96) * (31 ** i))
    
print(sum % 1234567891)