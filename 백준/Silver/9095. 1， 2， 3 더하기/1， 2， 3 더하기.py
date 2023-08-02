def recur(k, r):
    global count
    if sum(result) == r:
        count += 1
        return count
    if sum(result) > r:
        return
    for i in range(len(n)):
        result.append(n[i])
        recur(i, r)        
        result.pop()
    return count
T = int(input())

n = [1, 2, 3]
result = []

ary_list = []
for i in range(T):
    ary_list.append(int(input()))    
    
for i in range(T):
    count = 0
    print(recur(0, ary_list[i]))