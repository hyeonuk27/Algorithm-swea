import sys
sys.stdin = open('input.txt')

def sum_node(n):
    if n > N:
        return 0
    # 노드에 값이 있는 경우
    if tree[n]:
        return tree[n]
    # 노드에 값이 없는 경우
    return sum_node(2 * n) + sum_node(2 * n + 1)

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, v = map(int, input().split())
        tree[node] = v
    print('#%d %d' % (t, sum_node(L)))