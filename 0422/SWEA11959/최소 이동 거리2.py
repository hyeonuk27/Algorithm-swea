import sys
sys.stdin = open('input.txt')

def get_minV(D, V):
    minI, minV = 0, INF
    for i in range(N+1):
        if not V[i] and D[i] < minV:
            minI, minV = i, D[i]
    return minI

def dijkstra(s):
    D = [INF] * (N+1)
    V = [0] * (N+1)
    V[s] = 1

    for e, w in AL[s]:
        D[e] = w

    for _ in range(N):
        i = get_minV(D, V)
        for e, w in AL[i]:
            D[e] = min(D[e], D[i]+w)
    return D[N]

INF = 2e9
for t in range(1, int(input())+1):
    N, E = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        AL[s].append((e, w))
    print('#%d %d' % (t, dijkstra(0)))
