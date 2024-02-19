n = int(input())

x = n ** 0.5

if x % 1 == 0:
    print(int((x+1)**2))
else:
    print(-1)