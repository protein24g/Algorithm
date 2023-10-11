S = list(map(str, input()))
ary = []
for i in range(len(S)):
    ary.append(''.join(S[i:]))

ary.sort()
for i in ary:
    print(i)
