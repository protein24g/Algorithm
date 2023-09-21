n, m = map(int, input().split())
ary = []
for _ in range(n):
  ary.append(list(map(str, input())))
res = []
cnt = 0

for i in range(m):
  d = {}
  for j in range(n):
    d[ary[j][i]] = d.get(ary[j][i], 0) + 1
  d = sorted(d.items(), key = lambda x : (-x[1], x[0]))
  res.append(d[0][0])
  cnt += n - d[0][1]
  
print(''.join(res))
print(cnt)
