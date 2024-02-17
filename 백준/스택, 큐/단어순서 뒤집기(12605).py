import sys

n = int(sys.stdin.readline())

for i in range(n):
    STRING = sys.stdin.readline().split()
    print(f"Case #{i+1}: ", end="")
    for j in range(len(STRING)-1, -1, -1):
        print(STRING[j], end=" ")
    print()
    