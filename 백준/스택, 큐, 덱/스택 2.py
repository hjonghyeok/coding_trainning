import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    
    if x[0] == str(1):
        stack.append(x[1])
    elif x[0] == str(2):
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif x[0] == str(3):
        print(len(stack))
    elif x[0] == str(4):
        if stack:
            print(0)
        else:
            print(1)
    elif x[0] == str(5):
        if stack:
            print(stack[-1])
        else:
            print(-1)
