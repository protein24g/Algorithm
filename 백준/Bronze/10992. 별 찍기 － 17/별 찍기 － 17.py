n = int(input())
br = 1
for i in range(1, n):
    if n == 1: print('*')
    else:
        for j in range(n-i): print(' ',end='')
        print('*',end='')
        if i != 1:
            for j in range(br):
                print(' ',end='')
            br += 2
            print('*')
        else:
            print()
        
for i in range(n*2-1): print('*',end='')
