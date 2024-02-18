import sys

n, m = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))
answers = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] <= m:
                answers.append(cards[i]+cards[j]+cards[k])

print(max(answers))
