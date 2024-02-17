import sys

for i in range(int(sys.stdin.readline().strip())):
    test = sys.stdin.readline().strip()
    if test[0] != "(" or test[-1] != ")":
        print("NO")
    else:
        while 1:
            if "()" in test:
                test = test.replace("()","")
            else:
                if test == "":
                    print("YES")
                else:
                    print("NO")
                break
    