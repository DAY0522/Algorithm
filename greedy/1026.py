N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

# S가 최소가 되기 위해선 A의 가장 작은 값과 B의 가장 큰 값이 곱해지도록 해야함
A.sort()
B.sort(reverse=True)

sum = 0
# sol1
for i in range(N):
    sum += A[i] * B[i]
print(sum)

"""
# sol2
for _ in range(N):
    sum += min(A)*max(B)
    A.remove(min(A))
    B.remove(max(B))
print(sum)
"""
