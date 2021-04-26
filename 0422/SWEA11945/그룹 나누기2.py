import sys
sys.stdin = open('input.txt')

def rep(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[rep(y)] = rep(x)

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    vote = list(map(int, input().split()))
    for s, e in zip(vote[::2], vote[1::2]):
        union(s, e)
    ans = 0
    for i in range(len(p)):
        if i == p[i]:
            ans += 1
    print('#%d %d' % (t, ans-1))