n = input().split('-')
ary = []

for i in n:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    ary.append(sum)

res = ary[0]
for i in range(1, len(ary)):
    res -= ary[i]
print(res)
