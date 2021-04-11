import sys
sys.stdin = open('input.txt')

def subtree(n):
    global cnt
    cnt += 1
    if len(tree[n]) >= 1:
        subtree(tree[n][0])
    if len(tree[n]) == 2:
        subtree(tree[n][1])

for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    node = list(map(int, input().split()))
    for i in range(E):
        tree[node[2*i]].append(node[2*i+1])
    cnt = 0
    subtree(N)
    print('#%d %d' % (t, cnt))