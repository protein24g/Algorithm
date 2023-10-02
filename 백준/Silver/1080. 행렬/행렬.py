def chk(n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


n, m = map(int, input().split())
a, b = [], []
for i in range(n): a.append(list(map(int, input())))
for i in range(n): b.append(list(map(int, input())))

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnt += 1
            for K in range(i, i+3):
                for L in range(j, j+3):
                    if a[K][L] == 1: a[K][L] = 0
                    else: a[K][L] = 1
if chk(n, m): print(cnt)
else: print(-1)
