def fact(x):
  global count
  count += 1
  if count == N:
    return x
  x = x * fact(x-1)
  return x

T = int(input())
ary = []

for _ in range(T):
  N, M = list(map(int, input().split()))
  count = 0; a = fact(M)
  count = 0; b = fact(N)
  ary.append(a // b)

for i in range(len(ary)):
  print(ary[i])