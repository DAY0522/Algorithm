import sys
from itertools import combinations

while True:
    test = list(map(int, input().split(' '))) # 한 줄 입력시에는 input이 더 빠른 듯
    del test[0]

    if not test:
        exit()

    comb = list(combinations(test, 6)) # 조합 함수 이용
    for c in comb: # 조합된 원소 출력
        print(*c) # 컨테이너 앞에 *를 쓰면 컨테이너 기호 없이 출력됨
    print()