import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

answer = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            answer = True
        if answer:
            break
    if answer == True:
        print(x, y)
        break
    