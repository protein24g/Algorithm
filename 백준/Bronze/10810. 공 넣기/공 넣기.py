n, m = map(int, input().split())
ary = [0 for _ in range(n+1)]
for t in range(m):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        ary[n] = k
print(*ary[1:])
