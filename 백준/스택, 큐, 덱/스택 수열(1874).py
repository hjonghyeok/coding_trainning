import sys

n = int(input())

pop_list = [i for i in range(0, n+1)]
m = []
for _ in range(n):
    m.append(int(sys.stdin.readline().strip()))
    
idx = 1
stack = []
answer = []
an_stack = []
for i in m:
    if idx <= i:
        for j in range(idx, i+1):
            if pop_list[j] != 0:
                stack.append(j)
                pop_list[j] = 0
                answer.append("+")
            idx += 1
    if idx >= i:
        an_stack.append(stack.pop())
        answer.append("-")
        idx -= 1

if m == an_stack:
    for i in answer:
        print(i)
else:
    print("NO")
    
    
