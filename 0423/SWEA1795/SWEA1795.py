import sys
sys.stdin = open('input.txt')

def get_minV(D, V):
    minI, minV = 0, INF
    for i in range(N+1):
        if not V[i] and minV > D[i]:
            minI, minV = i, D[i]
    return minI

def dijkstra(sv, AL):
    V = [0] * (N + 1)
    D = [INF] * (N + 1)
    D[sv] = 0
    for _ in range(N):
        i = get_minV(D, V)
        V[i] = 1
        for e, w in AL[i]:
            D[e] = min(D[e], D[i] + w)
    return D[1:]

INF = 2e9
for t in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())
    AL1 = [[] for _ in range(N + 1)]
    AL2 = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        AL1[s].append((e, w))
        AL2[e].append((s, w))
    ans = max(a + b for a, b in zip(dijkstra(X, AL1), dijkstra(X, AL2)))
    print('#%d %d' % (t, ans))