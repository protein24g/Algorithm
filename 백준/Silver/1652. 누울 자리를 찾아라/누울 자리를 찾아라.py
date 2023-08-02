N = int(input())

ary = [list(input()) for _ in range(N)]

c = 0
row_result = 0
for i in range(N):
    for j in range(N):
        if ary[i][j] == '.':
            c += 1
            if c >= 2:
                if c == 2:
                    row_result += 1
        elif ary[i][j] == 'X':
            c = 0
    c = 0

c = 0
col_result = 0
for i in range(N):
    for j in range(N):
        if ary[j][i] == '.':
            c += 1
            if c >= 2:
                if c == 2:
                    col_result += 1
        elif ary[j][i] == 'X':
            c = 0
    c = 0; len = 0

print(row_result, col_result)