st = list(map(str, input()))
b = list(map(str, input()))
tmp = []
for i, j in enumerate(st):
    tmp.append(j)
    if tmp and j == b[-1]:
        if tmp[-len(b):] == b:
            for k in range(len(b)):
                tmp.pop()
if tmp: print(''.join(map(str, tmp)))
else: print('FRULA')
        
