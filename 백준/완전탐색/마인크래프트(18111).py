import sys

n, m, b = map(int, sys.stdin.readline().strip().split())
blocks = []
h = 0
w1 = 2
w2 = 1

time = [0 for _ in range(257)]

for _ in range(n):
    blocks.append(list(map(int, sys.stdin.readline().strip().split())))
    
for i in range(257):
    block = b
    for j in blocks:
        for k in j:
            if k <= i:
                time[i] += i - k
                block -= i - k
            else:
                time[i] += 2 * (k - i)
                block += k - i
    if block >= 0 and time[i] <= time[h]:
        h = i
print(time[h], h)