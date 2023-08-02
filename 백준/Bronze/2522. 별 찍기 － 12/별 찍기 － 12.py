n = int(input())
for i in range(1, n*2):
    if i <= n:
        for j in range(n-i):
            print(' ',end='')
        for j in range(i): print('*',end='')
    else:
        cnt = 0
        for j in range(i-n): print(' ',end=''); cnt +=1
        while cnt < n:
            print('*',end=''); cnt += 1
        
    print()
        
