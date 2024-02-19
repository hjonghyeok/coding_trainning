n = input().split('-')
num = []

for i in n:
    a = i.split('+')
    sum = 0
    for j in a:
        sum += int(j)
    num.append(sum)
result = num[0]
for i in num[1:]:
    result -= i
print(result)