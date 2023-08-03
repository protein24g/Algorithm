n = int(input())
ary = []
for i in range(n): ary.append(input())
ary = list(set(ary))
ary.sort()
ary.sort(key=len)
for i in ary: print(i)
    
