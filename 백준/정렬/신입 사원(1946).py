import sys

for _ in range(int(sys.stdin.readline())):
    member = []
    for __ in range(int(sys.stdin.readline())):
        member.append(list(map(int, sys.stdin.readline().split())))
    member.sort(key=lambda x:x[0])
    answer = len(member)
    x, y = member[0]
    for i, j in member:
        if x < i and y < j:
            answer -= 1
        else:
            y = j
        x = i
    print(answer)
            
            