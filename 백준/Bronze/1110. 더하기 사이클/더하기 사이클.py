N = list(map(int, input()))
cmp = []
for i in N:
    if len(N) == 1:
        cmp.append(0)
        cmp.append(N[0])
    else:
        cmp.append(i)

count = 0
while 1:
    if len(N) == 1:
        N.append(N[0])
        N[0] = 0
    else:
        sum = 0
        for i in N:
            sum += i
        result = list(map(int, str(sum)))
        N[0] = N[1]
        N[1] = result[-1]
        count += 1
        
        if N == cmp:
            print(count)
            break