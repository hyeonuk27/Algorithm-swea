import sys
sys.stdin = open('input.txt')

def subtree(n):
    global cnt
    cnt += 1
    for i in tree[n]:
        subtree(i)

for t in range(1, int(input())+1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for _ in range(e+2)]
    for i in range(e):
        tree[nodes[2*i]].append(nodes[2*i+1])
    cnt = 0
    subtree(n)
    print('#%d %d' % (t, cnt))