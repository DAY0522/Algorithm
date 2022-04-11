str_a, str_b = map(list, input().split(' '))
len_a, len_b = len(str_a), len(str_b)
m_diff = len_a

for i in range(len_b-(len_a-1)):
    diff = sum(1 for d in range(len_a) if str_a[d] != str_b[i+d])
    m_diff = min(diff, m_diff)

'''
구글링 통해 찾은 다른 방법.
while문에서 계속 del과 len을 구하다보니 더 오래 걸리는 듯
while len_a <= len(str_b):
    diff = sum(1 for d in range(len_a) if str_a[d] != str_b[d])
    m_diff = min(diff, m_diff)
    del str_b[0]
'''

print(m_diff)