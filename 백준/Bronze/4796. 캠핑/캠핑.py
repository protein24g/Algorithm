pas = 0
while True:
    pas += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0: break
    tmp = v // p
    tmp2 = v % p
    if l < tmp2: tmp2 = l
    print('Case ' + str(pas) + ': ' + str(tmp * l + tmp2))
