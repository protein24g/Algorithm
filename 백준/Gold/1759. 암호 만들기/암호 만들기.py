def recur(b):
    global L, C
    if len(result) == L:
        vo, co = 0, 0
        for k in range(L):
            if result[k] in consonant:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print(''.join(result))

    for i in range(b, C):
        result.append(ary[i])
        recur(i+1)
        result.pop()


L, C = list(map(int, input().split()))

ary = list(map(str, input().split()))
ary.sort()
result = []
consonant = ['a', 'e', 'i', 'o', 'u']

recur(0)