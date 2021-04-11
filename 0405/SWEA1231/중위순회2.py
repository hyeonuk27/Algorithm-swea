import sys
sys.stdin = open('input.txt')

def inorder(n):
    length = len(tree[n])
    if length >= 2:
        inorder(int(tree[n][1]))
    if length == 3:
        inorder(int(tree[n][2]))
    word.append(tree[n][0])

for t in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for n in range(N):
        tree[n+1] = input().split()[1:]

    word = []
    inorder(1)
    ans = ''.join(map(str, word))
    print('#%d %s' % (t, ans))
