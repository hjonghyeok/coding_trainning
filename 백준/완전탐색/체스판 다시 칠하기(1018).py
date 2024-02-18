import sys

n, m = map(int, sys.stdin.readline().split())

chess = []
num = []


for i in range(n):
    chess.append(sys.stdin.readline().strip())

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 != 0:
                    if chess[a][b] == "B":
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if chess[a][b] == "W":
                        draw1 += 1
                    else:
                        draw2 += 1
        num.append(draw1)            
        num.append(draw2)            
        
print(min(num))
