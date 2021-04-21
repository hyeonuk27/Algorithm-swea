import sys
sys.stdin = open('input.txt')

def DFS(sv):
    visited[sv] = 1
    travel.append(sv)
    for c in sorted(AL[sv]):
        if visited[c]: continue
        DFS(c)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    AL = [[] for _ in range(V + 1)]
    for s, e in zip(edges[::2], edges[1::2]):
        AL[s].append(e)
        AL[e].append(s)
    visited = [0] * (V + 1)
    travel = []
    DFS(1)
    print('#%d %s' % (t, '-'.join(map(str, travel))))