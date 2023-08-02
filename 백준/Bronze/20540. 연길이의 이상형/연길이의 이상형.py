import sys
input = sys.stdin.readline

n = input()
my = [['I', 'E'], ['S', 'N'], ['T', 'F'], ['J', 'P']]
result = ''
for i in range(len(n)-1):
    if n[i] == my[i][0]: result += my[i][1]
    else: result += my[i][0]
print(result)