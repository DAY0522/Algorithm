def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers)) # str로 변경
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    answer = int(''.join(numbers))
    
    return str(answer)