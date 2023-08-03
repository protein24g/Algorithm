import sys
input = sys.stdin.readline

m, n, k, w = list(map(int, input().split()))
a = []
b = [[0 for _ in range(n-w+1)] for _ in range(m-w+1)]
temp = []
for i in range(m):
    a.append(list(map(int, input().split())))

for i in range(m-w+1):
    for j in range(n-w+1):
        for k in range(w):
            for l in range(w):
                temp.append(a[k+i][l+j])
        temp.sort()
        b[i][j] = temp[len(temp)//2]
        temp.clear()

for row in b:
    for element in row:
        print(element, end=' ')
    print()
