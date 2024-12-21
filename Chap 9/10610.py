#전체코드

n = input()

if '0' not in n:
    print(-1)

else:
    number = ''.join(sorted(n, reverse=True))

    if int(number) % 30 == 0:
        print(number)
    else:
        print(-1)