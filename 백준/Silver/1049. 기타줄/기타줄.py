n, m = map(int, input().split())
ary = []
for _ in range(m):
    ary.append(list(map(int, input().split())))

six = sorted(ary, key = lambda x : x[0])
one = sorted(ary, key = lambda x : x[1])

if six[0][0] >=one[0][1] * 6:
    print(one[0][1] * n)
else:
    tmp = (n // 6) * six[0][0]
    if six[0][0] < one[0][1] * (n % 6):
        print(tmp + six[0][0])
    else:
        print(tmp + one[0][1] * (n % 6))
        
