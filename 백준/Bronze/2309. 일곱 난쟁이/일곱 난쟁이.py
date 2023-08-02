ary = []
sum = 0
for i in range(9):
    ary.append(int(input()))
    sum += ary[i]
ary.sort()

for i in range(9):
    for j in range(i+1, 9):
        if sum - (int(ary[i])+int(ary[j])) == 100:    
            x = ary[i]; y = ary[j]
            break
        
ary.remove(x)
ary.remove(y)

for i in range(len(ary)):
    print(ary[i])