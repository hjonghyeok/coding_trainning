import sys
n = int(sys.stdin.readline().strip())
sol = [int(sys.stdin.readline().strip()) for _ in range(n)]
sol.sort()
if n == 0:
    print(0)
else:
    m = int((n*0.15)+0.5)
    if m < 1:
        avg = int(sum(sol) / len(sol) + 0.5)
    else:
        avg = int(sum(sol[m:-m]) / (len(sol) - m*2) + 0.5)
    print(int(avg))
