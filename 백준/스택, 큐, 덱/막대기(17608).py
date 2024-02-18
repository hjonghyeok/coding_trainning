import sys

n = int(sys.stdin.readline())
H = []
for i in range(n):
    H.append(int(sys.stdin.readline()))

h = H[-1]
count = 1
for i in range(len(H)-1, -1, -1):
    if H[i] > h:
        count += 1
        h = H[i]

print(count)
