import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    mbti = sys.stdin.readline().strip().split()
    
    answer = 100
    
    if n>32:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    cnt = 0
                    if i == j or j == k or k == i:
                        continue
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]:
                            cnt += 1
                        if mbti[k][x] != mbti[j][x]:
                            cnt += 1
                        if mbti[i][x] != mbti[k][x]:
                            cnt += 1
                    answer = min(cnt, answer)
        print(answer)