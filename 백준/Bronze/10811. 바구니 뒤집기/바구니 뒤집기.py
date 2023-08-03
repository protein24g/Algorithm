n, m = map(int, input().split())
ary = [i for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    tmp = ary[a:b+1]
    tmp.reverse()
    ary[a:b+1] = tmp
print(*ary[1:])


