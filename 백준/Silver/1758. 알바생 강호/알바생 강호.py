n = int(input())
ary = []
for _ in range(n):
    ary.append(int(input()))
ary.sort(reverse=True)

res = 0
for i, j in enumerate(ary):
  tmp = j - ((i + 1) - 1)
  if tmp > 0:
    res += tmp
print(res)