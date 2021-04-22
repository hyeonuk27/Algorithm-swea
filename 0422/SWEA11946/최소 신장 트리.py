import sys
sys.stdin = open('input.txt')

def rep(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[rep(y)] = rep(x)

def kruskal():
    S = 0
    for s, e, w in edges:
        if rep(s) != rep(e):
            union(s, e)
            S += w
    return S

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    p = list(range(V+1))
    edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    print('#%d %d' % (t, kruskal()))