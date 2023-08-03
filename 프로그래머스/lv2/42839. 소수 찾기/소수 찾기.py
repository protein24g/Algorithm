from itertools import permutations
def solution(numbers):
    answer = []
    num = list(map(str, numbers))
    tmp = []
    tmp2 = []
    for i in range(1, len(numbers)+1):
        tmp += list(permutations(num, i))
    tmp2 = [int(''.join(p)) for p in tmp]
    
    for i in set(tmp2):
        if i < 2: continue
        chk = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                chk = 0
                break
        if chk: answer.append(i)
    
    return len(answer)