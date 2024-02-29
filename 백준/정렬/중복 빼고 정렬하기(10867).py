import sys

n = int(sys.stdin.readline())
arr = sorted(set(map(int, sys.stdin.readline().split())))
print(' '.join(map(str, arr)))