from itertools import permutations
while 1:
    try:
        a = list(map(str, input().split()))
        chk = 0
        for i, j in enumerate(permutations(a[0])):
            if i+1 == int(a[1]):
                chk = 1
                print(*a, '=', ''.join(j))
        else:
            if chk == 0: print(*a, '=', 'No permutation')
    except: break        
