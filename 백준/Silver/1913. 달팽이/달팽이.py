N = int(input())
A = int(input())
ary = [[0 for _ in range(N)] for _ in range(N)]
x = N // 2; y = N // 2
ary[x][y] = 1

cnt = 1
admin = 1
out = True

while out:
    for _ in range(admin):
        if 0 <= x-1 and out:
            x -= 1
            cnt += 1
            ary[x][y] = cnt
        else:
            out = False
    for _ in range(admin):
        if y+1 < N and out:
            y += 1
            cnt += 1
            ary[x][y] = cnt
        else:
            out = False 
    admin += 1
    for _ in range(admin):
        if x+1 < N and out:
            x += 1
            cnt += 1
            ary[x][y] = cnt
        else:
            out = False
    for _ in range(admin):
        if 0 <= y-1 and out:
            y -= 1
            cnt += 1
            ary[x][y] = cnt
        else:
            out = False    
    admin += 1

for i in range(N):
    for j in range(N):
        print(ary[i][j], end=' ')
    print()

for i in range(N):
    for j in range(N):
        if ary[i][j] == A:
            print(i+1, j+1)
            exit()