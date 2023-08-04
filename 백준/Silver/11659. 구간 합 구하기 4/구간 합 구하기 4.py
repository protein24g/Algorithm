import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))
s_ary = [0]
s = 0
for i in ary:
    s += i
    s_ary.append(s)
    
for i in range(m):
    a, b = map(int, input().split())
    print(s_ary[b] - s_ary[a-1])
