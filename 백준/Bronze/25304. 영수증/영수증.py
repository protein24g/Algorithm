x = int(input())
n = int(input())
s = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    s += a * b
if x == s: print('Yes')
else: print('No')