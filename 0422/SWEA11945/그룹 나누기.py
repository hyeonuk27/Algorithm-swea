import sys
sys.stdin = open('input.txt')

def rep(x):
    while x != p[x]:
        x = p[x]
    return x


def union_set(x, y):
    p[rep(y)] = rep(x)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    vote = list(map(int, input().split()))
    for a, b in zip(vote[::2], vote[1::2]):
        union_set(a, b)
    ans = -1
    for i, r in enumerate(p):
       if i == r:
           ans += 1
    print('#%d %d' % (t, ans))