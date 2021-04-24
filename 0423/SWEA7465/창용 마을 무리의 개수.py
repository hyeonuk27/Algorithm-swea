import sys
sys.stdin = open('input.txt')

def rep(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[rep(y)] = rep(x)


for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)
    cnt = sum(p[i] == i for i in range(1, N+1))
    print('#%d %d' % (t, cnt))