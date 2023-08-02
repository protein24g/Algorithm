def recur(b):
    if len(result) == 6:
        print(*result)
        return
    for i in range(b, len(ary)):
        result.append(ary[i])
        recur(i+1)
        result.pop()
result = []
tmp = []

while 1:
    ary = list(map(int, input().split()))
    if ary[0] == 0:
        break
    recur(1)
    print("")