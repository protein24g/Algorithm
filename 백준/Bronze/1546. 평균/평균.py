n = int(input())
ary = list(map(int, input().split()))
m = max(ary)
s = 0
for i in range(len(ary)):
    ary[i] =  ary[i]/m*100
print(sum(ary)/len(ary))
