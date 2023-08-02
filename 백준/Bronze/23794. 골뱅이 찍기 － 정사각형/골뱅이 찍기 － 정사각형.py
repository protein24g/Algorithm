N = int(input())

for i in range(N+2):
  print('@', end='')

for i in range(N):
  print('\n@', end='')
  for j in range(N):
    print(' ', end='')
  print('@', end='')
print()
for i in range(N+2):
  print('@', end='')
print()