import sys

n, m = map(int, sys.stdin.readline().strip().split())

dic = {}
L = []
for i in range(n):
    name = sys.stdin.readline().strip()
    dic[name] = i
    L.append(name)
    
for i in range(m):
    q = sys.stdin.readline().strip()
    try:
        q = int(q)
        print(L[q-1])
    except:
        print(dic.get(q)+1)