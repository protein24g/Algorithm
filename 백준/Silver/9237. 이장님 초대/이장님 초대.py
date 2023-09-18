n = int(input())
ary = list(map(int, input().split()))
ary.sort(reverse=True)
res = []
for i in range(n):
    res.append(ary[i] + i + 1)
print(max(res) + 1)
