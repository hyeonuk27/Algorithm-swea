import sys
sys.stdin = open('input.txt')

def inorder(n):
    l = len(tree[n])
    if l >= 2:
        inorder(int(tree[n][1]))
    word.append(tree[n][0])
    if l == 3:
        inorder(int(tree[n][2]))

for t in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(N):
        info = input().split()
        tree[i+1] = info[1:]

    word = []
    inorder(1)
    ans = ''.join(word)
    print('#%d %s' % (t, ans))