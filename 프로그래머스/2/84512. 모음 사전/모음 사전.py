from itertools import product

def solution(word):
    ary = ['A', 'E', 'I', 'O', 'U']
    res = []
    for i in range(1, 6):
        for j in product(ary, repeat = i):
            res.append(''.join(list(j)))
    res.sort()
    return res.index(word)+1