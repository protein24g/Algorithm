R, B = 0, 0
score = [10, 8, 6, 5, 4, 3, 2, 1, 0]
res = []
for i in range(8):    
    n = input()

    m = 60 * int(n.split(':')[0])
    s = int(n.split(':')[1])
    tmp = n.split(':')[2]
    tmp = tmp.split(' ')
    ms = int(tmp[0])
    team = tmp[1]
    res.append([m, s, ms, team])

res = sorted(res, key = lambda x : (x[0], x[1], x[2]))

for i in range(8):
    m, s, ms, team = res[i]
    if team == 'R':
        R += score[i]
    elif team == 'B':
        B += score[i]
if R > B:
    print('Red')
else:
    print('Blue')
    
