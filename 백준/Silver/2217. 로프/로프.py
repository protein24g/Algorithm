n = int(input())
ary = [int(input()) for _ in range(n)]
ary.sort(reverse = True)
res = []
for i in range(n):
    res.append(ary[i]*(i+1))
print(max(res))
