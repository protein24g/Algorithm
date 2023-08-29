import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
ary.sort()
res = 0
s = 0
for i in ary:
    s += i
    res += s
print(res)
