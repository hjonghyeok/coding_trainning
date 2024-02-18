import sys

n = int(input())
stack = []

for i in range(n):
    o = sys.stdin.readline().split()

    if o[0] == 'push':
        stack.append(o[1])
    elif o[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif o[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif o[0] == 'size':
        if not stack:
            print(0)
        else:
            print(len(stack))
    else:
        if not stack:
            print(1)
        else:
            print(0)