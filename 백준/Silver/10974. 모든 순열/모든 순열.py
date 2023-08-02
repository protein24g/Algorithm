from itertools import permutations
n = int(input())
ary = [i for i in range(1, n+1)]
for i in permutations(ary):
    print(*i)
