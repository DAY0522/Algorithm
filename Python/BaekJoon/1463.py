N = int(input())
arr = [0, 0, 1, 1]
for num in range(4, N+1):
    if num%6==0:
        arr.append(min(arr[num-1], arr[num//2], arr[num//3])+1)
    elif num%3==0:
        arr.append(min(arr[num - 1], arr[num // 3]) + 1)
    elif num%2==0:
        arr.append(min(arr[num - 1], arr[num // 2]) + 1)
    else:
        arr.append(arr[num-1]+1)
print(arr[N])