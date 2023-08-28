import sys
input = sys.stdin.readline

n = input().strip()

if n == 'P' or n == 'PPAP':
    print('PPAP')
else:
    st = []
    res = list('PPAP')
    for i in n:
        st.append(i)
        if st[-4:] == res:
            st.pop()
            st.pop()
            st.pop()
    if st == res or st == ['P']:
        print('PPAP')
    else:
        print('NP')
