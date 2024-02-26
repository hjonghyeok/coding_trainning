n, m = map(int, input().split())
a = [list(map(int, input().split()))  for _ in range(n) ]
b = [list(map(int, input().split()))  for _ in range(n) ]
sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum[i][j] = a[i][j] + b[i][j]
        
for i in sum:
    for j in i:
        print(j, end=' ')
    print()