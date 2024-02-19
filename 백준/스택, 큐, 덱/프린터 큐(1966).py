import sys

for _ in range(int(sys.stdin.readline().strip())):
    n, m = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    place = a.index(max(a))
    answer = 0
    
    while 1:
        if a[place] == max(a):
            a[place] = -1
            answer += 1
            
            if place == m:
                break
        place += 1
        if place >= len(a):
            place = 0
    print(answer)