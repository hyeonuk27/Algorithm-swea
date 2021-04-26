import sys
sys.stdin = open('input.txt')

def rep(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[rep(y)] = rep(x)

def kruskal():
    ans = 0
    cnt = 0
    for s, e, w in edges:
        if rep(s) != rep(e):
            union(s, e)
            ans += w
            cnt += 1
            if cnt == E - 1:
                break
    return ans

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    p = list(range(V+1))
    edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    print('#%d %d' % (t, kruskal()))
