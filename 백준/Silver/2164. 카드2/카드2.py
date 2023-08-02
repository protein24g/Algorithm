from collections import deque
ary = deque(i+1 for i in range(int(input())))
while len(ary) != 1:
    ary.popleft()
    ary.append(ary[0])
    ary.popleft()
print(*ary)
    
