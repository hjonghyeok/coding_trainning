import sys

queue = []

for _ in range(int(sys.stdin.readline().strip())):
    x = sys.stdin.readline().strip().split()
    if x[0] == 'push':
        queue.append(x[1])
    elif x[0] == 'pop':
        if queue == []:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if queue == []:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if queue == []:
            print(-1)
        else:
            print(queue[0])
    else:
        if queue == []:
            print(-1)
        else:
            print(queue[-1])