N, P = list(map(int, input().split()))

tmp = N
ary = []
while 1:
    tmp = (tmp * N) % P
    if tmp in ary:
        print(len(ary) - ary.index(tmp))
        break
    ary.append(tmp)