from collections import defaultdict
s1, s2, s3 = map(int, input().split())
d = defaultdict(int)

for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            d[i+1 + j+1 + k+1] += 1
d = sorted(d.items(), key=lambda x:x[0])
d = sorted(d, key=lambda x:x[1], reverse=True)
print(d[0][0])
