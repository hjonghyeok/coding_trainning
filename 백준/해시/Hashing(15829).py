key = 96
l = int(input())
s = input()
answer = 0
for i in range(l):
    answer += (ord(s[i]) - key) * (31 ** i)
print(answer % 1234567891)