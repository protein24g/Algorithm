import sys
input = sys.stdin.readline

n = input().rstrip()
cute = True

if len(n) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    diff = int(n[1]) - int(n[0])
    for i in range(2, len(n)):
        if int(n[i]) - int(n[i-1]) != diff:
            cute = False
            break
    if cute:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    else:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
