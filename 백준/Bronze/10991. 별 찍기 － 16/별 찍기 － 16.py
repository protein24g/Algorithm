n = int(input())
for i in range(1, n+1):
    if n == 1: print('*')
    else:
        for j in range(n-i): print(' ',end='')
        for j in range(0, i-1+1): print('* ',end='')
        print()
