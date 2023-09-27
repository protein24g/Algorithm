import sys
input = sys.stdin.readline

n = int(input())
ary = []
for i in range(n): ary.append(int(input()))
ary.sort()

s = 0
for i in range(n): s += abs((i+1) - ary[i])
print(s)
