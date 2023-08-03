while 1:
    ary = input()
    if ary == '0': break
    chk = 0
    left, right = 0, len(ary)-1
    while left < right:
        if ary[left] != ary[right]:
            chk = 1
            break
        left += 1; right -= 1
    if chk: print('no')
    else: print('yes')
