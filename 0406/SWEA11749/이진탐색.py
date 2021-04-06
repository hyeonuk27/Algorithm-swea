import sys
sys.stdin = open('input.txt')

def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)
        tree[n] = cnt
        cnt += 1
        inorder(n*2+1)

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1], tree[N//2]))