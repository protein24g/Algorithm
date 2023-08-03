from itertools import permutations
def solution(k, dungeons):
    answer = -1
    res = 0
    for i in permutations(dungeons):
        c, h = 0, k
        for j, l in enumerate(i):
            if h >= l[0]: c += 1; h -= l[1];
        res = max(c, res)
        
    return res