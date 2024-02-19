import sys
m = int(sys.stdin.readline().strip())
S = []
all = [ str(_) for _ in range(1, 21)]
for _ in range(m):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'add':
        if cmd[1] not in S:
            S.append(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in S:
            S.remove(cmd[1])
    elif cmd[0] == 'check':
        if cmd[1] in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.append(cmd[1])
    elif cmd[0] == 'all':
        S = all.copy()
    else:
        S = []