A, B = list(map(int, input().split()))
ary = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
a_r = []
c = 0
for i in range(1, len(ary)+1):
    tmp = A // ary[-i]
    if tmp > 0:
        c += tmp
        A %= ary[-i]
        a_r.append(ary[-i])

b_r = []
c = 0
for i in range(1, len(ary)+1):
    tmp = B // ary[-i]
    if tmp > 0:
        c += tmp
        B %= ary[-i]
        b_r.append(ary[-i])

s = 0
for i in range(len(a_r)):
    if a_r[i] not in b_r:
        s += a_r[i]

for i in range(len(b_r)):
    if b_r[i] not in a_r:
        s += b_r[i]
print(s)
    
