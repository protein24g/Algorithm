a, b = map(str, input().split())
ary_a = []
ary_b = []

for i in a:
    if i == '6':
        ary_a.append('5')
    else:
        ary_a.append(i)
for i in b:
    if i == '6':
        ary_b.append('5')
    else:
        ary_b.append(i)

print(int(''.join(ary_a)) + int(''.join(ary_b)), end=' ')

ary_a = []
ary_b = []
for i in a:
    if i == '5':
        ary_a.append('6')
    else:
        ary_a.append(i)
for i in b:
    if i == '5':
        ary_b.append('6')
    else:
        ary_b.append(i)

print(int(''.join(ary_a)) + int(''.join(ary_b)))

