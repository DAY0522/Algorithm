def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        first = phone_book[i]
        second = phone_book[i+1]
        if len(first) < len(second) and first == second[:len(first)]:
            return False
        
    return True

''' solution #2
def solution(phone_book):
    answer = True
    
    nums = {} # dictionary
    for num in phone_book:
        nums[num] = True
    
    for num in phone_book:
        for i in range(1, len(num)):
            if nums.get(num[:i]):
                return False
    
    return True
'''