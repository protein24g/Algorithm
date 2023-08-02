import math
ary = [0 for i in range(10)]

for i in list(map(int,input())):
    ary[i] += 1
ary[6] = math.ceil((ary[6]+ary[9])/2)
print(max(ary[:9]))