N, K = list(map(int, input().split()))

ary = list(map(int, input().split()))

mtt = []
count = 0

for i in range(K):
    if ary[i] in mtt:
        continue
    if len(mtt) != N:
        mtt.append(ary[i])
        continue

    far = 0
    tmp = 0

    for j in mtt:
        if j not in ary[i:]:
            tmp = j
            break
        elif ary[i:].index(j) > far:
            far = ary[i:].index(j)
            tmp = j
    mtt[mtt.index(tmp)] = ary[i]
    count += 1

print(count)