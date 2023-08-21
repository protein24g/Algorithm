from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
ary = []

for _ in range(n):ary.append(int(input()))

ary.sort()
print(round(sum(ary)/n))
print(ary[n//2])

tmp = Counter(ary).most_common()
if len(ary) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(max(ary) - min(ary))
