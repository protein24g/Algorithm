n = int(input())
ary = []
for _ in range(n): ary.append(list(map(str, input())))
for i in range(n):
    s = 0
    c = 1
    for j in range(len(ary[i])):
        if ary[i][j] == 'O': s += c; c += 1
        else: c = 1
    print(s)