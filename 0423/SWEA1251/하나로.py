import sys
sys.stdin = open('input.txt')

def get_minV(D, V):
    minI, minV = 0, INF
    for i in range(N):
        if not V[i] and minV > D[i]:
            minI, minV = i, D[i]
    return minI


def prim(s):
    D = [INF] * N
    V = [0] * N
    D[s] = 0
    for _ in range(N):
        i = get_minV(D, V)
        V[i] = 1
        for j in range(N):
            if not V[j]:
                D[j] = min(D[j], AM[i][j])
    return sum(D)


INF = float('inf')
for t in range(1, int(input())+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    T = float(input())
    AM = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N-1):
        for j in range(i+1, N):
            w = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            AM[i][j] = w
            AM[j][i] = w
    print('#%d %d' % (t, round(prim(0) * T)))
