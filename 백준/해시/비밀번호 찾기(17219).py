import sys

n, m = map(int, sys.stdin.readline().strip().split())
site = []
password = []

for _ in range(n):
    a = sys.stdin.readline().strip().split()
    site.append(a[0])
    password.append(a[1])
    
result = []
for _ in range(m):
    word = sys.stdin.readline().strip()
    result.append(password[site.index(word)])

for i in result:
    print(i)
