s = input()
cnt = 0
res = []
for i in s:
    if i != '.':
        cnt += 1
    else:
        if cnt % 2 != 0:
            print(-1)
            exit(0)
        tmp4 = cnt // 4
        cnt %= 4
        tmp2 = cnt // 2
        cnt %= 2
        for j in range(tmp4):
            res.append('AAAA')
        for j in range(tmp2):
            res.append('BB')
        res.append('.')
if cnt != 0:
    if cnt % 2 != 0:
        print(-1)
        exit(0)
    tmp4 = cnt // 4
    cnt %= 4
    tmp2 = cnt // 2
    cnt %= 2
    for j in range(tmp4):
        res.append('AAAA')
    for j in range(tmp2):
        res.append('BB')
    print(''.join(res))
else:
    print(''.join(res))
