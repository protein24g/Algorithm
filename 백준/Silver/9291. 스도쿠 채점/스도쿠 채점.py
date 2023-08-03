x = int(input())
for i in range(1, x+1):
    chk = 1
    ary = []
    for j in range(9):
        ary.append(list(map(int, input().split())))
    for j in range(9):
        visited = [0 for _ in range(10)]
        for k in range(9):
            visited[ary[j][k]] += 1
        if max(visited[1:]) > 1 or min(visited[1:]) < 1:
            chk = 0
    for j in range(9):
        visited = [0 for _ in range(10)]
        for k in range(9):
            visited[ary[k][j]] += 1
        if max(visited[1:]) > 1 or min(visited[1:]) < 1:
            chk = 0
    for j in range(3):
        for k in range(3):
            visited = [0 for _ in range(10)]
            nj, nk = j * 3, k * 3
            for r1 in range(3):
                for r2 in range(3):
                    visited[ary[nj+r1][nk+r2]] += 1
            if max(visited[1:]) > 1 or min(visited[1:]) < 1:
                chk = 0 

    if chk:
        print('Case %d: CORRECT'%(i))
    else:
        print('Case %d: INCORRECT'%(i))
    if i != x: trash = input()
                

