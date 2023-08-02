import sys
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

st = list()
for i in range(n):
    while st and k > 0 and st[-1] < s[i]:
        st.pop()
        k -= 1
    st.append(s[i])

print("".join(st[:len(st) - k]))

