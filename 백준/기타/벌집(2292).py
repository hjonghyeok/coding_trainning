# n = int(input())

# nums_pileup = 1 
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  
#     cnt += 1 
# print(cnt)


for _ in range(int(input())):
    h, w, n = map(int, input().split())
    b = []
    c = n%h
    if c == 0:
        c = h
    b.append(str(c))
    if n % h == 0:
        a = n//h
    else:
        a = n//h + 1 
    if a < 10:
        b.append('0'+str(a))
    else:
        b.append(str(a))
    print(''.join(b))