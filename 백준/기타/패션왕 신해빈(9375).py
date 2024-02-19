import sys

for _ in range(int(sys.stdin.readline().strip())):
    clothes = [sys.stdin.readline().strip().split() for i in range(int(sys.stdin.readline().strip()))]
    
    clothes_type = {}
    
    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
    cnt = 1
    for num in clothes_type.values():
        cnt *= num
    print(cnt - 1)
            