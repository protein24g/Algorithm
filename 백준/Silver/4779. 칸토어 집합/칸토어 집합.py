import sys
input = sys.stdin.readline

while 1:
    try:
        n = int(input())
        if n == 0: print('-')
        elif n == 1: print('- -')
        else:
            size = 3**n
            ary = ['-' for _ in range(size)]
            div = size // 3
            while div != 0:
                for i in range(1, (size // div) + 1):
                    if i % 2 == 0:
                        for j in range(div*(i-1), div*i):
                            ary[j] = ' '
                div //= 3
            print(''.join(ary))
    except:
        break
            

