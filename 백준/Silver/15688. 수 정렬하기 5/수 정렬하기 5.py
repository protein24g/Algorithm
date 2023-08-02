import sys
N = int(sys.stdin.readline())
arrayList = []
for i in range(N):
    x = int(sys.stdin.readline())
    arrayList.append(x)
sortedList = sorted(arrayList, reverse = False)
for i in range(N):
    print(sortedList[i])