from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
ary = sorted([input().rstrip() for _ in range(n)])
res = set()
for i in permutations(ary, k):
    res.add(''.join(i))
print(len(res))
