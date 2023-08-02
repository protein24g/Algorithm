n, m = map(int, input().split())
ary = [i for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    tmp = ary[a]
    ary[a] = ary[b]
    ary[b] = tmp
print(*ary[1:])
