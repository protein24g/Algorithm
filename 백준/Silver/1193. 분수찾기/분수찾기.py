x = int(input())

start, stop, cnt = 1, 1, 0
cur_i, cur_j = 1, 1

while x != 1:
    cnt += 1
    stop = (4 * cnt) + 1 + start
    if start <= x <= stop:
        cur_j = cur_j + (2 * (cnt - 1)) # start j
        cnt = start
        while 1:
            #오른쪽
            cur_j += 1
            cnt += 1
            if cnt == x: print('%d/%d'%(cur_i, cur_j)); exit(0)

            #대각 왼쪽 아래
            while cur_j != 1:
                cur_i += 1; cur_j -= 1
                cnt += 1
                if cnt == x: print('%d/%d'%(cur_i, cur_j)); exit(0)

            #아래쪽
            cur_i += 1;
            cnt += 1
            if cnt == x: print('%d/%d'%(cur_i, cur_j)); exit(0)

            #대각 오른쪽 위
            while cur_i != 1:
                cur_i -= 1; cur_j += 1
                cnt += 1
                if cnt == x: print('%d/%d'%(cur_i, cur_j)); exit(0)

    else:
        start = stop
if x == 1:
    print('1/1')
