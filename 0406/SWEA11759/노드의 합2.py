import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    for i in range(N, L, -1):
        tree[i//2] += tree[i]
    print('#%d %d' % (t, tree[L]))