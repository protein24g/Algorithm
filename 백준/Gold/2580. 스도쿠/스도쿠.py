def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            for j in range(9):
                print(ary[i][j], end=' ')
            print()
        exit()
    init = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
    a, b = zero[cnt]
    for i in range(9):
        if ary[a][i] in init: # 가로 확인
            init.remove(ary[a][i])
        if ary[i][b] in init: # 세로 확인
            init.remove(ary[i][b])

    nx, ny = a // 3 * 3, b // 3 * 3
    for i in range(3): # 구간 확인
        for j in range(3):
            if ary[i+nx][j+ny] in init:
                init.remove(ary[i+nx][j+ny])

    if len(init) != 0:
        for i in range(len(init)):
            ary[a][b] = init[i]
            dfs(cnt+1)
            ary[a][b] = 0

ary = [list(map(int, input().split())) for _ in range(9)]

zero = []

for i in range(9):
    for j in range(9):
        if ary[i][j] == 0:
            zero.append([i, j])
dfs(0)