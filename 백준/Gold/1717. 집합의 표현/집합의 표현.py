import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def u_p(x, y):
    x = g_p(union[x])
    y = g_p(union[y])

    if x < y:
        union[y] = x
    else:
        union[x] = y

def g_p(x):
    if union[x] == x:
        return x
    else:
        union[x] = g_p(union[x])
        return union[x]

def f_p(x, y):
    x = g_p(union[x])
    y = g_p(union[y])

    if x == y:
        return 1
    else:
        return 0

n, m = list(map(int, input().split()))
union = [0 for _ in range(n+1)]
for i in range(1, n+1):
    union[i] = i

for i in range(m):
    c, a, b = list(map(int, input().split()))
    if c == 0:
        u_p(a, b)
    else:
        if f_p(a, b):
            print("YES")
        else:
            print("NO")
