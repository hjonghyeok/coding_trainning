import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

target = 'IO' * n
target += 'I'

cnt = 0
for i in range(len(s)):
    if target == s[i:i + len(target)]:
        cnt += 1
        
print(cnt)