n = int(input())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
ary = sorted(ary, key = lambda x : (x[0], x[1]))

tmp = -1
for i in range(n):
    if tmp <= ary[i][0]:
        tmp = ary[i][0] + ary[i][1]
    else:
        tmp += ary[i][1]
print(tmp)
