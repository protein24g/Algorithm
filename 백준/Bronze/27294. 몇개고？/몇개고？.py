T, S = list(map(int, input().split()))

if 0 <= T <= 11:
    time = 'morning'
elif 12 <= T <= 16:
    time = 'lunch'
else:
    time = 'dinner'

if S == 1 or time != 'lunch':
    print('280')
elif time == 'lunch' and S == 0:
    print('320')