ary = []  
for _ in range(int(input())):
    ary.append(list(map(int, input().split())))
ary.sort()
cost = 1e9
res = 0
for i in ary:
    tmp = i[1]
    if tmp < cost:
        cost = tmp
        res += 1
print(res)