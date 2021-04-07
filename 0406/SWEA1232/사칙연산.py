import sys
sys.stdin = open('input.txt')

operator = {'+': (lambda x, y: x + y),
          '-': (lambda x, y: x - y),
          '*': (lambda x, y: x * y),
          '/': (lambda x, y: x / y),
}

def postorder(n):
    if len(tree[n]) > 1:
        o, l, r = tree[n]
        return operator[o](postorder(int(l)), postorder(int(r)))
    return int(tree[n][0])

for t in range(1, 11):
    N = int(input())
    tree = [''] + [input().split()[1:] for _ in range(N)]
    ans = int(postorder(1))
    print('#%d %d' % (t, ans))