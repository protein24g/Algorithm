def cmp(large, num):
  if large <= num:
    large = num
  return large

def find_row_col(large, i, j):
  C, P, Z, Y = 0, 0, 0, 0
  # 가로 줄 사탕 확인
  for m in range(N):
    if ary[i][m] == 'C':
      C += 1; P, Z, Y = 0, 0, 0
      large = cmp(large, C)
    if ary[i][m] == 'P':
      P += 1; C, Z, Y = 0, 0, 0
      large = cmp(large, P)
    if ary[i][m] == 'Z':
      Z += 1; C, P, Y = 0, 0, 0
      large = cmp(large, Z)
    if ary[i][m] == 'Y':
      Y += 1; C, P, Z = 0, 0, 0
      large = cmp(large, Y)

  C, P, Z, Y = 0, 0, 0, 0
  # 세로 줄 사탕 확인
  for m in range(N):
    if ary[m][j] == 'C':
      C += 1; P, Z, Y = 0, 0, 0
      large = cmp(large, C)
    if ary[m][j] == 'P':
      P += 1; C, Z, Y = 0, 0, 0
      large = cmp(large, P)
    if ary[m][j] == 'Z':
      Z += 1; C, P, Y = 0, 0, 0
      large = cmp(large, Z)
    if ary[m][j] == 'Y':
      Y += 1; C, P, Z = 0, 0, 0
      large = cmp(large, Y)

  return large

N = int(input())
ary = [list(input()) for _ in range(N)]

large = 0
for i in range(N):
  for j in range(N):
    # 아래로 갈 수 있다면
    if i+1 != N:
      # swap
      tmp = ary[i][j]
      ary[i][j] = ary[i+1][j]
      ary[i+1][j] = tmp

      large = find_row_col(large, i, j)
      large = find_row_col(large, i+1, j)
      
      # 아래 되돌리기
      tmp = ary[i][j]
      ary[i][j] = ary[i+1][j]
      ary[i+1][j] = tmp
      
    # 오른쪽 으로 갈 수 있다면
    if j+1 != N:
      # swap
      tmp = ary[i][j]
      ary[i][j] = ary[i][j+1]
      ary[i][j+1] = tmp

      large = find_row_col(large, i, j)
      large = find_row_col(large, i, j+1)
      
      # 오른쪽 되돌리기
      tmp = ary[i][j]
      ary[i][j] = ary[i][j+1]
      ary[i][j+1] = tmp
      
print(large)