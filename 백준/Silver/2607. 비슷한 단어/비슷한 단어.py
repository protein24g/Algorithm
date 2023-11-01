N = int(input())
target = list(input())
res = 0

for _ in range(N-1):
    ary = target[:] 
    word = input()
    cnt = 0
    for w in word:
        if w in ary: ary.remove(w)
        else:cnt += 1
    if cnt < 2 and len(ary) < 2:
        res += 1
print(res)
