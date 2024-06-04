def solution(N, number):
    result = [9] * 32001
    dict = {}
    
    for n in range(1, 9):
        dict[n] = {int(str(N)*n)}
        for i in range(1, n//2+1):
            a, b = i, n-i
            calculator(n, a, b, dict)
        if number in dict[n]:
            return n
    
    return -1

def calculator(n, a, b, dict):
    operator = ['+', '-', '/', '*']
    for o in operator:
        if o == '+' or o == '*':
            for left in dict[a]:
                for right in dict[b]:
                    if o == '+':
                        dict[n].add(left + right)
                    else:
                        dict[n].add(left * right)

        else:
            for left in dict[a]:
                for right in dict[b]:
                    if o == '-':
                        dict[n].add(left - right)
                        dict[n].add(right - left)
                    else:
                        if right != 0:
                            dict[n].add(left // right)
                        if left != 0:
                            dict[n].add(right // left)
