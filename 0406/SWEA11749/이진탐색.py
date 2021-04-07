import sys
sys.stdin = open('input.txt')

def inorder(n):
    global i
    if n <= N:
        inorder(2 * n)
        tree[n] = i
        i += 1
        inorder(2 * n + 1)

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N + 1)
    i = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1], tree[int(N/2)]))