import sys
sys.stdin = open('input.txt')

def Dijkstra(s):
    D = [987654321] * (N+1)
    V = [0] * (N+1)
    V[s] = 1

    for e, w in AL[s]:
        D[e] = w

    for _ in range(N):
        minW = 987654321
        for i in range(N+1):
            if not V[i] and minW > D[i]:
                idx, minW = i, D[i]
        V[idx] = 1
        for e, w in AL[idx]:
            D[e] = min(D[e], D[idx] + w)
    return D[N]


for t in range(1, int(input())+1):
    N, E = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        AL[s].append((e, w))
    print('#%d %d' % (t, Dijkstra(0)))