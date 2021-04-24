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
    cnt = 0
    for s, e, w in edges:
        if rep(s) != rep(e):
            union(s, e)
            S += w
            cnt += 1
            if cnt == N - 1:
                break
    return S


for t in range(1, int(input())+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    T = float(input())
    p = list(range(N+1))
    edges = []
    for i in range(N-1):
        for j in range(i+1, N):
            w = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            edges.append([i, j, w])
    edges = sorted(edges, key = lambda x: (x[2]))
    print('#%d %d' % (t, round(kruskal() * T)))