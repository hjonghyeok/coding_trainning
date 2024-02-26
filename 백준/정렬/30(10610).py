n = input()
n = sorted(n, reverse = 1)
if '0' not in n:
    print(-1)
else:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3:
        print(-1)
    else:
        print(''.join(n))