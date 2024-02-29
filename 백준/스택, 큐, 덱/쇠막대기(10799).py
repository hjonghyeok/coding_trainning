import sys
L = sys.stdin.readline().strip()

result = 0
stack = []
idx = 0
while idx < len(L):
    if L[idx] == '(':
        if L[idx+1] == ')':
            result += len(stack)
            idx += 2
            continue
        else:
            stack.append(L[idx])
    else:
        result += 1
        stack.pop()
    idx += 1
        
print(result)