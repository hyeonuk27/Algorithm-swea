import sys
sys.stdin = open('input.txt')

def BFS(sv):
    Q = [sv]
    visited = [0] * (V + 1)
    visited[sv] = 1
    while Q:
        node = Q.pop(0)
        travel.append(node)
        for c in AL[node]:
            if visited[c]: continue
            visited[c] = 1
            Q.append(c)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for i in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    travel = []
    BFS(1)
    print('#%d %s' % (t, ' '.join(map(str, travel))))