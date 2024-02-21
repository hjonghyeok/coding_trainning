import sys

P = [0] * 101
L = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(1, len(L)):
    P[i] = L[i]
for i in range(11, 101):
    P[i] = P[i-1] + P[i-5]
    
for _ in range(int(sys.stdin.readline())):
    print(P[int(sys.stdin.readline())])