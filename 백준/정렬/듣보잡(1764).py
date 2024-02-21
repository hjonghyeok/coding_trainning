import sys

n, m = map(int, sys.stdin.readline().strip().split())

A = set()
answers = []
for i in range(n):
    A.add(sys.stdin.readline().strip())

for i in range(m):
    name = sys.stdin.readline().strip()
    if name in A:
        answers.append(name)
        
print(len(answers))
answers.sort()
for i in answers:
    print(i)
    