def recur(k, b):
    global maax
    if k == 3:
        if M >= sum(result) and maax <= sum(result):
            maax = sum(result)
            #print(result)
        return maax
    for i in range(b, len(ary)):
        result.append(ary[i])
        recur(k+1, i+1)
        result.pop()
    return maax
    
    
N, M = list(map(int, input().split()))

ary = list(map(int, input().split()))
r = 3
maax = 0
result = []

print(recur(0, 0))