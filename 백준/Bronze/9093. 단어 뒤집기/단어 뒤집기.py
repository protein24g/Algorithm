t = int(input())
for i in range(t):
    ary = list(map(str, input().split()))
    for j in ary:
        print(j[::-1], end=' ')
    print()
    
