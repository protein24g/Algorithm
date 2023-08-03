import sys
input = sys.stdin.readline

def binary_search(t):
    left, right = 0, len(ary)-1
    while left <= right:
        mid = (left + right) // 2
        if ary[mid] == t:
            return 1
        elif ary[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return 0

N = int(input())
ary = list(map(int, input().split()))
ary.sort()
M = int(input())
target = list(map(int, input().split()))

for i in target:
    print(binary_search(i))
