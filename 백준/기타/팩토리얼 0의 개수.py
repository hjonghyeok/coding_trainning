n = int(input())

f = 1
for i in range(1, n+1):
    f *= i
    
cnt = 0

for i in str(f)[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)