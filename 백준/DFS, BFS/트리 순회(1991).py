import sys

n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    root, l, r = sys.stdin.readline().strip().split()
    tree[root] = l, r

def dfs(node):
    if node != '.':
        print(node, end="")        
        dfs(tree[node][0])
        dfs(tree[node][1])

def dfs2(node):
    if node != '.':
        dfs2(tree[node][0])
        print(node, end="")        
        dfs2(tree[node][1])

def dfs3(node):
    if node != '.':
        dfs3(tree[node][0])
        dfs3(tree[node][1])
        print(node, end="")        


dfs('A')
print()
dfs2('A')
print()
dfs3('A')