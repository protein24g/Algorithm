from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
m = int(input())
f_ary = list(map(int, input().split()))

res = Counter(ary)
for i in f_ary:
    if i in res: print(res[i], end=' ')
    else: print(0, end=' ')