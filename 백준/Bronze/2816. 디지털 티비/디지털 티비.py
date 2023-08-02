N = int(input())
ary = []

for i in range(N):
   ary.append(input())

chk = 0
cur = 0

if ary[0] != 'KBS1':
  while ary[cur] != 'KBS1':
    print('1', end='')
    cur += 1
      
  while cur != 0:
    print('4', end='')
    tmp = ary[cur-1]
    ary[cur-1] = ary[cur]
    ary[cur] = tmp
    cur -= 1
    
if ary[1] != 'KBS2':
  while ary[cur] != 'KBS2':
    print('1', end='')
    cur += 1
    
  while cur != 1:
    print('4', end='')
    tmp = ary[cur-1]
    ary[cur-1] = ary[cur]
    ary[cur] = tmp
    cur -= 1