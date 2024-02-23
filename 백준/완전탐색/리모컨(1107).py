import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
n_button = list(map(int, sys.stdin.readline().split()))

result = abs(n - 100)

for i in range(0, 1000001):
    swich = False
    for j in str(i):
        if int(j) in n_button:
            swich = True
    if not swich:
        b = len(str(i)) + abs(n - i)
        result = min(b, result)
    
print(result)