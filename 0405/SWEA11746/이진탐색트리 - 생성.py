import sys
sys.stdin = open('input.txt')

# 이진탐색트리 생성
def make_BST(pn, cn):
    if pn > cn: # 좌
        if tree[pn][0]:
            return make_BST(tree[pn][0], cn)
        tree[pn][0] = cn
    else: # 우
        if tree[pn][1]:
            return make_BST(tree[pn][1], cn)
        tree[pn][1] = cn

# 전위순회
def preorder(n):
    if n:
        ans.append(n)
        preorder(tree[n][0])
        preorder(tree[n][1])

N = int(input())
nodes = list(map(int, input().split()))
tree = [[0, 0] for _ in range(max(nodes)+1)]
root = nodes[0]
for i in range(1, N):
    make_BST(root, nodes[i])

ans = []
preorder(root)
print('-'.join(map(str, ans)))
